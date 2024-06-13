import argparse
import subprocess
import sys
from os import environ, fspath
from pathlib import Path

from rich.console import Console

console = Console()


def print_color(message: str):
    prefix = "[ sim_and_k4run ]:"
    console.print(f"{prefix} {message}", style="bold yellow")


def validate_args(args):
    if (
        args.detector_version not in detver_lookup1
        or args.detector_version not in detver_lookup2
    ):
        raise ValueError(f"Invalid detector version: {args.detector_version}")


def set_environment():
    environ["k4geo_dir"] = fspath(Path.home() / "promotion/code/k4geo/")
    print_color("Switched to local k4geo")


def build_ddsim_command(args, sim_file, log_file_base):
    base_cmd = (
        f"ddsim --outputFile {sim_file} "
        f"--compactFile {environ['k4geo_dir']}{detver_lookup1[args.detector_version]} "
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
        f"--detectorModel={detver_lookup2[args.detector_version]} "
        f"--outputFileBase={output_file_base} "
        "--noBeamCalReco --trackingOnly"
    )

    if args.logmode:
        return f"{base_cmd} > {log_file_base}_k4run.log 2>&1"
    if not args.verbose:
        return f"{base_cmd} &> /dev/null"
    return base_cmd


def execute_command(cmd):
    print_color(f"Executing command: {cmd}")
    subprocess.run(cmd, shell=True, check=True)


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

        data_dir = Path("data/")
        log_dir = Path("log/")
        sim_output_file_path = (
            data_dir / f"{args.name}_{args.detector_version}_SIM.edm4hep.root"
        )
        rec_output_file_base = data_dir / f"{args.name}_{args.detector_version}"
        log_file_base = log_dir / f"{args.name}_{args.detector_version}"

        set_environment()
        print_color(f"Output will be written to: {sim_output_file_path}")

        ddsim_cmd = build_ddsim_command(args, sim_output_file_path, log_file_base)
        if not args.dry_run:
            execute_command(ddsim_cmd)

        k4run_cmd = build_k4run_command(
            args, sim_output_file_path, rec_output_file_base, log_file_base
        )
        if not args.dry_run:
            execute_command(k4run_cmd)

        if args.dry_run:
            print_color("Dry mode activated: Commands printed but not executed")
        else:
            print_color("Both commands executed successfully")
    except ValueError as e:
        print_color(str(e))
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print_color(f"Command failed: {e}")
        sys.exit(e.returncode)


detver_lookup1 = {
    "v02": "ILD/compact/ILD_sl5_v02/ILD_l5_o1_v02.xml",
    "v09": "ILD/compact/ILD_sl5_v02/ILD_l5_o1_v09.xml",
    "v11": "ILD/compact/ILD_l5_v11/ILD_l5_v11.xml",
}

detver_lookup2 = {"v02": "ILD_l5_o1_v02", "v09": "ILD_l5_o1_v09", "v11": "ILD_l5_v11"}

if __name__ == "__main__":
    main()
