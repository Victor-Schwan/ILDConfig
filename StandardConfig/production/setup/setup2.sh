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
source env/bin/activate
print_color "fix PYTHONPATH"
export PYTHONPATH=$(pwd):$PYTHONPATH

print_color "MARLIN_DLL with custom: MarlinTrkProcessors and my Viewer"
export MARLIN_DLL=/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/pandoraanalysis/61b8993d121e84efa07bd74678b2ef687597ba77_develop-ql5wqr/lib/libPandoraAnalysis.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/marlinmlflavortagging/902342aa6adca9af9e14e34da396886e238cc417_develop-yl2cwj/lib/libMarlinMLFlavorTagging.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/marlinkinfitprocessors/3da6620dcedd015a64e133761562e639b701736f_develop-zy7l5w/lib/libMarlinKinfitProcessors.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/ildperformance/ac928d9cf774d702e396aac0c41df2987e4b27a5_develop-zkxcvt/lib/libILDPerformance.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/garlic/3.1-xxjfhh/lib/libGarlic.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/forwardtracking/bd6ef3f58dc601266a835d1344682cbf94710de3_develop-zjrd4y/lib/libForwardTracking.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/clupatra/1.3.1-qksn34/lib/libClupatra.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/clicperformance/67f13e53a3b4d9322e17c6705bef363f4f05aa92_develop-c6blua/lib/libClicPerformance.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/overlay/edf53447c7d2d3f4d784dae5c1c8bee17abdf30a_develop-kxpafq/lib/libOverlay.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/marlinreco/c9e266db8a7e80b791163fb877793cf96ce883cb_develop-2xgedv/lib/libMarlinReco.so:/home/vector/promotion/code/MarlinTrkProcessors/build/lib/libMarlinTrkProcessors.so.2.12.5:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/marlinkinfit/0fb147401f1761282f28452704ff89a61bc331e5_develop-isb7un/lib/libMarlinKinfit.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/marlinfastjet/1582bd2eac7996ea9d75a573bdab276daed4653e_develop-2vwkf4/lib/libMarlinFastJet.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/lctuple/0a8162a702da7cd57b44057ae17879a9c171bc02_develop-4hnn3w/lib/libLCTuple.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/lcfiplus/39cf1736f3f05345dc67553bca0fcc0cf64be43e_develop-t2b4cd/lib/libLCFIPlus.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/fcalclusterer/13d14611fe39032f0b6bacde043f8e057e28234f_develop-xyvgjx/lib/libFCalClusterer.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/marlindd4hep/715b4e5789f2d91027df6c4190a9260e5eb690f9_develop-qlcxfe/lib/libMarlinDD4hep.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/ddmarlinpandora/747bb1f34c34184783aed8a38a928bec515a0b88_develop-7kxdgj/lib/libDDMarlinPandora.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/conformaltracking/b0b9e4815400ece9a7dab187cf72479d84bd2795_develop-7hwpor/lib/libConformalTracking.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-08-21/x86_64-ubuntu22.04-gcc11.4.0-opt/cedviewer/50c041343a4b069f7a7458e7d98267f349465bc2_develop-4n3v3o/lib/libCEDViewer.so:/home/vector/promotion/code/viewer/lib/libMyViewerProc.so:
