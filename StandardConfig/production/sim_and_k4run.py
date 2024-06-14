import argparse
import subprocess
import sys
from dataclasses import dataclass
from os import environ, fspath
from pathlib import Path

# from rich.console import Console

# console = Console()


# Define the dataclass
@dataclass
class DetectorVersion:
    short_name: str
    tech_name: str
    compact_file_path: Path


def print_color(message: str):
    prefix = "[ sim_and_k4run ]:"
    # console.print(f"{prefix} {message}", style="bold yellow")
    print(f"{prefix} {message}")


def validate_args(args):
    if args.detector_version not in detector_versions:
        raise ValueError(f"Invalid detector version: {args.detector_version}")


def set_environment():
    environ["k4geo_DIR"] = fspath(Path.home() / "promotion/code/k4geo/")
    print_color("Switched to local k4geo")


def build_ddsim_command(args, sim_file, log_file_base):
    base_cmd = (
        f"ddsim --outputFile {sim_file} "
        f"--compactFile {environ['k4geo_DIR'] / detector_versions[args.detector_version].compact_file_path} "
        "--steeringFile TPC_debug_muon_steer.py"
    )

    if args.logmode:
        return f"{base_cmd} > {log_file_base}_ddsim.log 2>&1"
    if not args.verbose:
        return f"{base_cmd} &> /dev/null"
    return base_cmd


def build_k4run_command(args, sim_file, output_file_base, log_file_base):
    base_cmd = (
        f"k4run ILDReconstruction.py -n -1 --inputFiles={sim_file} --lcioOutput on "
        f"--detectorModel={detector_versions[args.detector_version].tech_name} "
        f"--outputFileBase={output_file_base} "
        "--noBeamCalReco --trackingOnly"
    )

    if args.logmode:
        return f"{base_cmd} > {log_file_base}_k4run.log 2>&1"
    if not args.verbose:
        return f"{base_cmd} &> /dev/null"
    return base_cmd


def execute_command(cmd, cmd_nickname):
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
        "--logmode",
        action="store_true",
        help="Enable log mode to redirect output to log files",
    )
    return parser.parse_args()


def main():
    try:
        args = parse_arguments()
        validate_args(args)

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

        set_environment()

        ddsim_cmd = build_ddsim_command(args, sim_output_file_path, log_file_base)

        k4run_cmd = build_k4run_command(
            args, sim_output_file_path, rec_output_file_base, log_file_base
        )

        print_color(f"Simulation output will be written to: {sim_output_file_path}")

        if args.dry_run:
            print_color("Dry mode activated: Commands printed but not executed")
            print_color(f"ddsim cmd: {ddsim_cmd}")
            print_color(f"k4run cmd: {k4run_cmd}")

        else:
            execute_command(ddsim_cmd, "ddsim")
            execute_command(k4run_cmd, "k4run")

        print_color("Both commands executed successfully")

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
}

if __name__ == "__main__":
    main()
