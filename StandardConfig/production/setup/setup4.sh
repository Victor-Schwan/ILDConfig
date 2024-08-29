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

print_color "source k4n"
k4n

print_color "fix PYTHONPATH"
export PYTHONPATH=$(pwd):$PYTHONPATH

print_color "source env venv"
source $HOME/promotion/code/ILDConfig/StandardConfig/production/env/bin/activate

print_color "added MyViewerProc to mdll"
export MARLIN_DLL=$MARLIN_DLL/home/vector/promotion/code/viewer/lib/libMyViewerProc.so:
