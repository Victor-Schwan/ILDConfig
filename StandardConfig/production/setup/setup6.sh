# Function to print messages in specified color
print_color() {
    # ANSI yellow
    local YELLOW='\033[1;33m'
    # ANSI no color (reset)
    local NC='\033[0m'
    local PREFIX="[ setup ]:"
    echo
    echo -e "${YELLOW}${PREFIX}${NC} $1"
    echo
}

print_color "k4n"
k4n

print_color "set myCodeDir env var"
export myCodeDir="$HOME/promotion/code"

print_color "set local k4geo"
export k4geo_DIR="$k4gDir"
export K4GEO="$k4gDir"

print_color "fix PYTHONPATH"
export PYTHONPATH=$(pwd):$PYTHONPATH

print_color "source env venv"
source $myCodeDir/ILDConfig/StandardConfig/production/env/bin/activate

print_color "add FCC Plotting Style"
export PYTHONPATH=$PYTHONPATH:$HOME/promotion/code/
