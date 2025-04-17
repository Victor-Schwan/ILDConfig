#!/bin/bash

##################################
# example command: ./sim_and_k4run.sh trialRun v11 [v|verbose] [d|dry-run] [l|logmode]
##################################
DataDir="data/"
LogDir="log/"

# Function to print messages in specified color
print_color() {
    # ANSI yellow
    local YELLOW='\033[1;33m'
    # ANSI no color (reset)
    local NC='\033[0m'
    local PREFIX="[ sim_and_k4run ]:"
    echo
    echo -e "${YELLOW}${PREFIX}${NC} $1"
    echo
}

unset k4geo_DIR
export k4geo_DIR="$HOME/promotion/code/k4geo/"
print_color "Switched to local k4geo"

VERBOSE=0
DRY_MODE=0
LOG_MODE=0

for arg in "$@"; do
    if [[ "$arg" == "v" || "$arg" == "verbose" ]]; then
        VERBOSE=1
    elif [[ "$arg" == "d" || "$arg" == "dry-run" ]]; then
        DRY_MODE=1
    elif [[ "$arg" == "l" || "$arg" == "logmode" ]]; then
        LOG_MODE=1
    fi
done

# Check if the necessary number of arguments are passed (adjust as since the verbose flag is now an option)
if [[ "$#" -lt 2 ]]; then
    print_color "Usage: $0 <Name> <DetectorVersion> [v|verbose] [d|dry-run] [l|logmode]"
    exit 1
fi

# Assign arguments to variables for clearer access
Name=$1
DetVer=$2
SIM_file_name=${DataDir}${Name}_${DetVer}_SIM.edm4hep.root
LOG_FILE_BASE=${LogDir}${Name}_${DetVer}
print_color "Output will be written to: $SIM_file_name"

declare -A DetVer_LookUp1
declare -A DetVer_LookUp2

DetVer_LookUp1["v02"]="ILD/compact/ILD_sl5_v02/ILD_l5_o1_v02.xml"
DetVer_LookUp1["v09"]="ILD/compact/ILD_sl5_v02/ILD_l5_o1_v09.xml"
DetVer_LookUp1["v11"]="ILD/compact/ILD_l5_v11/ILD_l5_v11.xml"

DetVer_LookUp2["v02"]="ILD_l5_o1_v02"
DetVer_LookUp2["v09"]="ILD_l5_o1_v09"
DetVer_LookUp2["v11"]="ILD_l5_v11"

# Verify that the provided DetVer is valid
if [[ -z ${DetVer_LookUp1[$DetVer]} ]] || [[ -z ${DetVer_LookUp2[$DetVer]} ]]; then
    print_color "Invalid detector version: $DetVer"
    exit 1
fi

# Build the ddsim command
ddsim_cmd="ddsim --outputFile $SIM_file_name --compactFile $k4geo_DIR${DetVer_LookUp1[$DetVer]} --steeringFile TPC_debug_muon_steer.py"
# ddsim_cmd="ddsim --inputFiles Examples/bbudsc_3evt/bbudsc_3evt.stdhep --outputFile $SIM_file_name --compactFile $k4geo_DIR/${DetVer_LookUp1[$DetVer]} --steeringFile ddsim_steer.py"
if [[ $LOG_MODE -eq 1 ]]; then
    ddsim_cmd+=" > "${LOG_FILE_BASE}_ddsim.log" 2>&1"  # Redirect output to log file
elif [[ $VERBOSE -eq 0 ]]; then
    ddsim_cmd+=" &> /dev/null"  # Suppress output if VERBOSE is 0
fi
print_color "Executing command: $ddsim_cmd"

if [[ $DRY_MODE -eq 0 ]]; then
    eval $ddsim_cmd
    EXIT_CODE=$?
    if [ $EXIT_CODE -ne 0 ]; then
        print_color "ddsim command failed with exit code $EXIT_CODE"
        exit $EXIT_CODE
    fi
fi

k4run_cmd="k4run ILDReconstruction.py -n -1 --inputFiles=$SIM_file_name --lcioOutput on --detectorModel=${DetVer_LookUp2[$DetVer]} --outputFileBase=${DataDir}${Name}_${DetVer} --noBeamCalReco --trackingOnly"
if [[ $LOG_MODE -eq 1 ]]; then
    k4run_cmd+=" > "${LOG_FILE_BASE}_k4run.log" 2>&1"  # Redirect output to log file
elif [[ $VERBOSE -eq 0 ]]; then
    k4run_cmd+=" &> /dev/null"  # Suppress output if VERBOSE is 0
fi
print_color "Executing command: $k4run_cmd"

if [[ $DRY_MODE -eq 0 ]]; then
    eval $k4run_cmd
    EXIT_CODE=$?
    if [ $EXIT_CODE -ne 0 ]; then
        print_color "k4run command failed with exit code $EXIT_CODE"
        exit $EXIT_CODE
    fi
fi

if [[ $DRY_MODE -eq 1 ]]; then
    print_color "Dry mode activated: Commands printed but not executed"
else
    print_color "Both commands executed successfully"
fi