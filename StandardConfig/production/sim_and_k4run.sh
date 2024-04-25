#!/bin/bash

########################################
#
# if the muon gun is not used any longer, change names!?
# if more ifs to commands, built the commands in several steps instead of one step with many ifs?
#
# example command: ./sim_and_k4run.sh debugTPCedm4hep v11 [-v]
#
########################################

DataDir="data/"

# Function to print messages in specified color and make sure there's an empty line before and after the message
print_color() {
    # ANSI yellow
    local YELLOW='\033[1;33m'
    # ANSI no color (reset)
    local NC='\033[0m'
    # Prefix for identification
    local PREFIX="[ sim_and_k4run ]:"
    # Print empty line, colored message with prefix, and another empty line
    echo
    echo -e "${YELLOW}${PREFIX}${NC} $1"
    echo
}

# Check if the verbose flag is set
VERBOSE=0
for arg in "$@"; do
    if [[ "$arg" == "-v" || "$arg" == "--verbose" ]]; then
        VERBOSE=1
    fi
done

# Check if the necessary number of arguments are passed (adjust as since the verbose flag is now an option)
if [[ "$#" -lt 2 ]]; then
    print_color "Usage: $0 <Name> <DetVer> [-v|--verbose]"
    exit 1
fi

# Assign arguments to variables for clearer access
Name=$1
DetVer=$2
SIM_file_name=${DataDir}${Name}_${DetVer}_SIM.slcio
print_color "Output will be written to: $SIM_file_name"

# Define associative arrays for DetVer_LookUp1 and DetVer_LookUp2
declare -A DetVer_LookUp1
declare -A DetVer_LookUp2

# Populate the lookup tables
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
ddsim_cmd="ddsim --outputFile $SIM_file_name --compactFile $k4geo_DIR/${DetVer_LookUp1[$DetVer]} --steeringFile TPC_debug_muon_steer.py"
[[ $VERBOSE -eq 0 ]] && ddsim_cmd+=" &> /dev/null"

# Print and execute ddsim command
print_color "Executing command: $ddsim_cmd"
eval $ddsim_cmd
EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
    print_color "ddsim command failed with exit code $EXIT_CODE"
    exit $EXIT_CODE
fi

# Build the k4run command
k4run_cmd="k4run ILDReconstruction.py --inputFiles=$SIM_file_name --lcioOutput off --detectorModel=${DetVer_LookUp2[$DetVer]} --outputFileBase=${DataDir}${Name}_${DetVer} --noBeamCalReco --trackingOnly"
[[ $VERBOSE -eq 0 ]] && k4run_cmd+=" &> /dev/null"

# Print and execute k4run command
print_color "Executing command: $k4run_cmd"
eval $k4run_cmd
EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
    print_color "k4run command failed with exit code $EXIT_CODE"
    exit $EXIT_CODE
fi

print_color "Both commands executed successfully"