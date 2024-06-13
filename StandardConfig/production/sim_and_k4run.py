import argparse
import os
import subprocess
import sys
from pathlib import Path


def print_color(message: str):
    YELLOW = "\033[1;33m"
    NC = "\033[0m"
    PREFIX = "[ sim_and_k4run ]:"
    print(f"\n{YELLOW}{PREFIX}{NC} {message}\n")


def main():
    parser = argparse.ArgumentParser(description="Simulate and run k4 simulation.")
    parser.add_argument("Name", type=str, help="Name of the trial run")
    parser.add_argument("DetectorVersion", type=str, help="Version of the detector")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose mode"
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Perform a dry run without executing commands",
    )
    parser.add_argument(
        "-l",
        "--logmode",
        action="store_true",
        help="Enable log mode to redirect output to log files",
    )

    args = parser.parse_args()

    DataDir = Path("data/")
    LogDir = Path("log/")

    Name = args.Name
    DetVer = args.DetectorVersion
    VERBOSE = args.verbose
    DRY_MODE = args.dry_run
    LOG_MODE = args.logmode

    SIM_file_name = DataDir / f"{Name}_{DetVer}_SIM.edm4hep.root"
    LOG_FILE_BASE = LogDir / f"{Name}_{DetVer}"

    print_color(f"Switched to local k4geo")
    os.environ["k4geo_DIR"] = str(Path(os.environ["HOME"]) / "promotion/code/k4geo/")

    print_color(f"Output will be written to: {SIM_file_name}")

    DetVer_LookUp1 = {
        "v02": "ILD/compact/ILD_sl5_v02/ILD_l5_o1_v02.xml",
        "v09": "ILD/compact/ILD_sl5_v02/ILD_l5_o1_v09.xml",
        "v11": "ILD/compact/ILD_l5_v11/ILD_l5_v11.xml",
    }

    DetVer_LookUp2 = {
        "v02": "ILD_l5_o1_v02",
        "v09": "ILD_l5_o1_v09",
        "v11": "ILD_l5_v11",
    }

    if DetVer not in DetVer_LookUp1 or DetVer not in DetVer_LookUp2:
        print_color(f"Invalid detector version: {DetVer}")
        sys.exit(1)

    ddsim_cmd = f"ddsim --outputFile {SIM_file_name} --compactFile {os.environ['k4geo_DIR']}{DetVer_LookUp1[DetVer]} --steeringFile TPC_debug_muon_steer.py"
    if LOG_MODE:
        ddsim_cmd += f" > {LOG_FILE_BASE}_ddsim.log 2>&1"
    elif not VERBOSE:
        ddsim_cmd += " &> /dev/null"

    print_color(f"Executing command: {ddsim_cmd}")

    if not DRY_MODE:
        result = subprocess.run(ddsim_cmd, shell=True)
        if result.returncode != 0:
            print_color(f"ddsim command failed with exit code {result.returncode}")
            sys.exit(result.returncode)

    k4run_cmd = f"k4run ILDReconstruction.py -n -1 --inputFiles={SIM_file_name} --lcioOutput on --detectorModel={DetVer_LookUp2[DetVer]} --outputFileBase={DataDir / f'{Name}_{DetVer}'} --noBeamCalReco --trackingOnly"
    if LOG_MODE:
        k4run_cmd += f" > {LOG_FILE_BASE}_k4run.log 2>&1"
    elif not VERBOSE:
        k4run_cmd += " &> /dev/null"

    print_color(f"Executing command: {k4run_cmd}")

    if not DRY_MODE:
        result = subprocess.run(k4run_cmd, shell=True)
        if result.returncode != 0:
            print_color(f"k4run command failed with exit code {result.returncode}")
            sys.exit(result.returncode)

    if DRY_MODE:
        print_color("Dry mode activated: Commands printed but not executed")
    else:
        print_color("Both commands executed successfully")


if __name__ == "__main__":
    main()
