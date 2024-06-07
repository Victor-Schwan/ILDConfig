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
print_color "set local k4geo"
export k4geo_DIR="$HOME/promotion/code/k4geo"
# print_color "use local conformal tracking"
# export MARLIN_DLL="/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/pandoraanalysis/61b8993d121e84efa07bd74678b2ef687597ba77_develop-wffwbm/lib/libPandoraAnalysis.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/marlinkinfitprocessors/3da6620dcedd015a64e133761562e639b701736f_develop-jvdncz/lib/libMarlinKinfitProcessors.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/ildperformance/ac928d9cf774d702e396aac0c41df2987e4b27a5_develop-pvhdip/lib/libILDPerformance.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/garlic/3.1-gip7jh/lib/libGarlic.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/forwardtracking/bd6ef3f58dc601266a835d1344682cbf94710de3_develop-gm6akq/lib/libForwardTracking.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/clupatra/1.3.1-l7bhuf/lib/libClupatra.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/clicperformance/96196b8ba6cda62d69acd77989bd671320d37d5e_develop-gvgtfo/lib/libClicPerformance.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/overlay/edf53447c7d2d3f4d784dae5c1c8bee17abdf30a_develop-s3hylv/lib/libOverlay.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/marlintrkprocessors/5503ee6a012e56e71e18c46f9cbe765e626b7d24_develop-dnvhns/lib/libMarlinTrkProcessors.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/marlinreco/5c8162cf2362c5a5a5815032bb469f07ff506031_develop-prw6m3/lib/libMarlinReco.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/marlinkinfit/0fb147401f1761282f28452704ff89a61bc331e5_develop-susfly/lib/libMarlinKinfit.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/marlinfastjet/1582bd2eac7996ea9d75a573bdab276daed4653e_develop-mkhpx5/lib/libMarlinFastJet.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/lctuple/0a8162a702da7cd57b44057ae17879a9c171bc02_develop-l3ymjw/lib/libLCTuple.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/lcfiplus/39cf1736f3f05345dc67553bca0fcc0cf64be43e_develop-acpujp/lib/libLCFIPlus.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/fcalclusterer/13d14611fe39032f0b6bacde043f8e057e28234f_develop-ofedln/lib/libFCalClusterer.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/marlindd4hep/715b4e5789f2d91027df6c4190a9260e5eb690f9_develop-g3nkak/lib/libMarlinDD4hep.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/ddmarlinpandora/747bb1f34c34184783aed8a38a928bec515a0b88_develop-dmocz2/lib/libDDMarlinPandora.so:/home/vector/promotion/code/ConformalTracking/lib/libConformalTracking.so:/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2024-05-03/x86_64-ubuntu22.04-gcc11.4.0-opt/cedviewer/eec6d2391ca5bd735e402eb17de192863f959d62_develop-pxjuqp/lib/libCEDViewer.so:"
