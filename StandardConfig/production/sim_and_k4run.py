import argparse
import subprocess
import sys
from dataclasses import dataclass
from os import environ, fspath, getenv
from pathlib import Path

from rich.console import Console

console = Console()


# Define the dataclass
@dataclass
class DetectorVersion:
    short_name: str
    tech_name: str
    compact_file_path: Path


def print_color(message: str):
    prefix = "[ sim_and_k4run ]:"
    console.print(f"[bold yellow]{prefix}[/bold yellow] {message}")


def validate_args(args, command_list):
    if args.detector_version not in detector_versions:
        raise ValueError(f"Invalid detector version: {args.detector_version}")
    if args.command_index is not None:
        if args.command_index < 0 or args.command_index >= len(command_list):
            raise ValueError(
                f"Invalid command index: {args.command_index}. Must be between 0 and {len(command_list) - 1}."
            )


def set_environment():
    local_k4geo_path = Path.home() / "promotion/code/k4geo/"
    environ["k4geo_DIR"] = fspath(local_k4geo_path)
    environ["K4GEO"] = fspath(local_k4geo_path)
    print_color("Switched to local k4geo")


def check_k4geo_path():
    k4geo = getenv("K4GEO") or getenv("k4geo_DIR")
    if not k4geo:
        raise KeyError("Set a k4geo environment variable!")

    k4geo_path = Path(k4geo)
    if k4geo_path.is_relative_to("/cvmfs/"):
        print_color("k4geo from cvmfs used")
    elif k4geo_path.is_relative_to(Path.home()):
        print_color("local k4geo is used")
    else:
        print_color("unknown k4geo path used")


def log_mode_handler(args, base_cmd, log_file_base):
    if args.log_mode:
        base_cmd.append(f"> {log_file_base}.log 2>&1")
        return " ".join(base_cmd)
    if not args.verbose:
        base_cmd.append("&> /dev/null")
        return " ".join(base_cmd)
    return " ".join(base_cmd)


def build_ddsim_command(args, sim_file, log_file_base):
    base_cmd = [
        "ddsim",
        f"--outputFile {sim_file}",
        f"--compactFile {environ['k4geo_DIR'] / detector_versions[args.detector_version].compact_file_path}",
    ]

    if args.process_bbudsc:
        base_cmd.extend(
            [
                "--inputFiles Examples/bbudsc_3evt/bbudsc_3evt.stdhep",
                "--steeringFile ddsim_steer.py",
            ]
        )
    else:
        base_cmd.append("--steeringFile TPC_debug_muon_steer.py")

    return log_mode_handler(
        args, base_cmd, log_file_base.with_stem(log_file_base.stem + "_ddsim")
    )


def build_k4run_command(args, sim_file, output_file_base, log_file_base):
    base_cmd = [
        "k4run ILDReconstruction.py",
        "-n -1",
        f"--inputFiles={sim_file}",
        f"--lcioOutput {args.lcioOutput}",
        f"--detectorModel={detector_versions[args.detector_version].tech_name}",
        f"--outputFileBase={output_file_base}",
        "--noBeamCalRec",
        "--trackingOnly",
    ]

    return log_mode_handler(
        args, base_cmd, log_file_base.with_stem(log_file_base.stem + "_k4run")
    )


def process_command(cmd, cmd_nickname, dry_run):
    if dry_run:
        cmd_color = "cyan"
        print_color(
            f"Dry mode activated: [{cmd_color}]{cmd_nickname} cmd:[/{cmd_color}] {cmd}"
        )
    else:
        print_color(f"Executing command: {cmd_nickname}")
        subprocess.run(cmd, shell=True, check=True)
        print_color(f"Finished command: {cmd_nickname}")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Simulate and run k4 simulation.")
    parser.add_argument("name", type=str, help="Name of the trial run")
    parser.add_argument("detector_version", type=str, help="Version of the detector")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose mode"
    )
    parser.add_argument(
        "-d",
        "--dry_run",
        action="store_true",
        help="Perform a dry run without executing commands",
    )
    parser.add_argument(
        "-l",
        "--log_mode",
        action="store_true",
        help="Enable log mode to redirect output to log files",
    )
    parser.add_argument(
        "--process_bbudsc",
        action="store_true",
        help="When given, the 'standard' bbudsc_3evt file is processed.",
    )
    parser.add_argument(
        "--lcioOutput",
        help="Choose whether to still create LCIO output (off by default)",
        choices=["off", "on", "only"],
        default="off",
        type=str,
    )
    parser.add_argument(
        "-x",
        "--command_index",
        type=int,
        help="Execute only the specified command in the chain (0 for ddsim, 1 for k4run)",
    )
    return parser.parse_args()


def main():

    try:
        args = parse_arguments()

        # create Paths
        data_dir = Path("data/")
        log_dir = Path("log/")
        assert data_dir.exists(), f"The data directory '{data_dir}' does not exist."
        assert log_dir.exists(), f"The log directory '{log_dir}' does not exist."

        sim_output_file_path = (
            data_dir / f"{args.name}_{args.detector_version}_SIM.edm4hep.root"
        )
        rec_output_file_base = data_dir / f"{args.name}_{args.detector_version}"
        log_file_base = log_dir / f"{args.name}_{args.detector_version}"
        print_color(f"Simulation output will be written to: {sim_output_file_path}")

        set_environment()

        check_k4geo_path()

        # Create command list
        command_list = [
            ("ddsim", build_ddsim_command(args, sim_output_file_path, log_file_base)),
            (
                "k4run",
                build_k4run_command(
                    args, sim_output_file_path, rec_output_file_base, log_file_base
                ),
            ),
        ]
        validate_args(args, command_list)

        if args.command_index is None:
            for nickname, cmd in command_list:
                process_command(cmd, nickname, args.dry_run)
        else:
            process_command(*reversed(command_list[args.command_index]), args.dry_run)

        if not args.dry_run:
            print_color("Selected commands executed successfully")

    except ValueError as e:
        print_color(str(e))
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print_color(f"Command failed: {e}")
        sys.exit(e.returncode)


detector_versions = {
    "v02": DetectorVersion(
        short_name="v02",
        tech_name="ILD_l5_o1_v02",
        compact_file_path=Path("ILD/compact/ILD_sl5_v02/ILD_l5_o1_v02.xml"),
    ),
    "v09": DetectorVersion(
        short_name="v09",
        tech_name="ILD_l5_o1_v09",
        compact_file_path=Path("ILD/compact/ILD_sl5_v02/ILD_l5_o1_v09.xml"),
    ),
    "v11": DetectorVersion(
        short_name="v11",
        tech_name="ILD_l5_v11",
        compact_file_path=Path("ILD/compact/ILD_l5_v11/ILD_l5_v11.xml"),
    ),
    "if1": DetectorVersion(
        short_name="if1",
        tech_name="ILD_FCCee_v01",
        compact_file_path=Path(
            "FCCee/ILD_FCCee/compact/ILD_FCCee_v01/ILD_FCCee_v01.xml"
        ),
    ),
    "if2": DetectorVersion(
        short_name="if2",
        tech_name="ILD_FCCee_v02",
        compact_file_path=Path(
            "FCCee/ILD_FCCee/compact/ILD_FCCee_v02/ILD_FCCee_v02.xml"
        ),
    ),
}

if __name__ == "__main__":
    main()
