#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper
from Gaudi.Configuration import DEBUG, INFO

CT_MAX_DIST = "0.03;"  # semi-colon is important! RANDOM VALUE COPYIED FROM CLDRECO
MCPartColName = ["MCParticle"]  # MCParticleCollectionName
VertexBarrelHitCollectionNames = ["VertexBarrelTrackerHits"]
VertexEndcapHitCollectionNames = ["VertexEndcapTrackerHits"]

###################################################################
# Either TruthTrackFinder can run or ConformalTracking and ClonesAndSplitTracksFinder see CLDReco
###################################################################
#
# MyTruthTrackFinder = MarlinProcessorWrapper("MyTruthTrackFinder")
# MyTruthTrackFinder.OutputLevel = DEBUG
# MyTruthTrackFinder.ProcessorType = "TruthTrackFinder"
# MyTruthTrackFinder.Parameters = {
#     "FitForward": ["true"],
#     "MCParticleCollectionName": MCPartColName,
#     "SiTrackCollectionName": ["SiTracks"],
#     "SiTrackRelationCollectionName": ["SiTrackRelations"],
#     "SimTrackerHitRelCollectionNames": [
#         "VertexBarrelTrackerHitRelations ",
#         "InnerTrackerBarrelHitRelations",
#         "SETTrackerHitRelations",
#         "VertexEndcapTrackerHitRelations",
#         "InnerTrackerEndcapHitRelations",
#     ],
#     "TrackerHitCollectionNames": [
#         "VertexBarrelTrackerHits",
#         "InnerTrackerBarrelHits",
#         "SETTrackerHits",
#         "VertexEndcapTrackerHits",
#         "InnerTrackerEndcapHits",
#     ],
#     "UseTruthInPrefit": ["false"],
# }

MyClupatraProcessor = MarlinProcessorWrapper("MyClupatraProcessor")
MyClupatraProcessor.OutputLevel = INFO
MyClupatraProcessor.ProcessorType = "ClupatraProcessor"
MyClupatraProcessor.Parameters = {
    "Chi2Cut": ["100"],
    "CreateDebugCollections": ["false", "true"],
    "DistanceCut": ["40"],
    "DuplicatePadRowFraction": ["0.1"],
    "EnergyLossOn": ["true"],
    "MaxDeltaChi2": ["35"],
    "MaxStepWithoutHit": ["6"],
    "MinLayerFractionWithMultiplicity": ["0.5"],
    "MinLayerNumberWithMultiplicity": ["3"],
    "MinimumClusterSize": ["6"],
    "MultipleScatteringOn": ["false", "true"],
    "NumberOfZBins": ["150"],
    "OutputCollection": ["ClupatraTracks"],
    "PadRowRange": ["15"],
    "SITHitCollection": ["SITTrackerHits"],
    "SegmentCollectionName": ["ClupatraTrackSegments"],
    "SmoothOn": ["false"],
    "TPCHitCollection": ["TPCTrackerHits"],
    "TrackEndsOuterCentralDist": ["25"],
    "TrackEndsOuterForwardDist": ["40"],
    "TrackIsCurlerOmega": ["0.001"],
    "TrackStartsInnerDist": ["25"],
    "TrackSystemName": ["DDKalTest"],
    "VXDHitCollection": ["VertexBarrelTrackerHits", "VertexEndcapTrackerHits"],
    "pickUpSiHits": ["false"],
}

MyConformalTracking = MarlinProcessorWrapper("MyConformalTracking")
MyConformalTracking.OutputLevel = DEBUG
MyConformalTracking.ProcessorType = "ConformalTrackingV2"
MyConformalTracking.Parameters = {
    "DebugHits": ["DebugHits"],
    "DebugPlots": ["false"],
    "DebugTiming": ["false"],
    "MCParticleCollectionName": MCPartColName,
    "MaxHitInvertedFit": ["0"],
    "MinClustersOnTrackAfterFit": ["3"],
    "RelationsNames": [
        "VertexBarrelTrackerHitRelations",
        "VertexEndcapTrackerHitRelations",
        "InnerTrackerBarrelHitRelations",
        "InnerTrackerEndcapHitRelations",
    ],
    "RetryTooManyTracks": ["false"],
    "SiTrackCollectionName": ["SiTracksCT"],
    "SortTreeResults": ["true"],
    # fmt: off
    "Steps": [
        "[VertexBarrel]",
        "@Collections", ":", "VertexBarrelTrackerHits",
        "@Parameters", ":", "MaxCellAngle", ":", "0.01;", "MaxCellAngleRZ", ":", "0.01;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", CT_MAX_DIST, "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;",
        "@Flags", ":", "HighPTFit,", "VertexToTracker",
        "@Functions", ":", "CombineCollections,", "BuildNewTracks",
        "[VertexEncap]",
        "@Collections", ":", "VertexEndcapTrackerHits",
        "@Parameters", ":", "MaxCellAngle", ":", "0.01;", "MaxCellAngleRZ", ":", "0.01;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", CT_MAX_DIST, "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;",
        "@Flags", ":", "HighPTFit,", "VertexToTracker",
        "@Functions", ":", "CombineCollections,", "ExtendTracks",
        "[Tracker]",
        "@Collections", ":", "InnerTrackerBarrelHits,", "InnerTrackerEndcapHits",
        "@Parameters", ":", "MaxCellAngle", ":", "0.1;", "MaxCellAngleRZ", ":", "0.1;", "Chi2Cut", ":", "2000;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", CT_MAX_DIST, "SlopeZRange:", "10.0;", "HighPTCut:", "1.0;",
        "@Flags", ":", "HighPTFit,", "VertexToTracker,", "RadialSearch",
        "@Functions", ":", "CombineCollections,", "ExtendTracks",
    ],
    # fmt: on
    "ThetaRange": ["0.05"],
    "TooManyTracks": ["100000"],
    "TrackerHitCollectionNames": [
        "InnerTrackerBarrelHits",
        "InnerTrackerEndcapHits",
    ]
    + VertexBarrelHitCollectionNames
    + VertexEndcapHitCollectionNames,
    "trackPurity": ["0.7"],
    "VertexBarrelHitCollectionNames": VertexBarrelHitCollectionNames,
    "VertexEndcapHitCollectionNames": VertexEndcapHitCollectionNames,
}

# copied from https://github.com/gaswk/CLDConfig/blob/main/CLDConfig/CLDReconstruction.py
MyClonesAndSplitTracksFinder = MarlinProcessorWrapper("MyClonesAndSplitTracksFinder")
MyClonesAndSplitTracksFinder.OutputLevel = INFO
MyClonesAndSplitTracksFinder.ProcessorType = "ClonesAndSplitTracksFinder"
MyClonesAndSplitTracksFinder.Parameters = {
    "EnergyLossOn": ["true"],
    "InputTrackCollectionName": ["SiTracksCT"],
    "MultipleScatteringOn": ["true"],
    "OutputTrackCollectionName": ["SiTracks"],
    "SmoothOn": ["false"],
    "extrapolateForward": ["true"],
    "maxSignificancePhi": ["3"],
    "maxSignificancePt": ["2"],
    "maxSignificanceTheta": ["3"],
    "mergeSplitTracks": ["false"],
    "minTrackPt": ["1"],
}

MyRefit = MarlinProcessorWrapper("MyRefit")
MyRefit.OutputLevel = INFO
MyRefit.ProcessorType = "RefitFinal"
MyRefit.Parameters = {
    "EnergyLossOn": ["true"],
    "InputRelationCollectionName": ["SiTrackRelations"],
    "InputTrackCollectionName": ["SiTracks"],
    "Max_Chi2_Incr": ["1.79769e+30"],
    "MinClustersOnTrackAfterFit": ["3"],
    "MultipleScatteringOn": ["true"],
    "OutputRelationCollectionName": ["SiTracks_Refitted_Relation"],
    "OutputTrackCollectionName": ["SiTracks_Refitted"],
    "ReferencePoint": ["-1"],
    "SmoothOn": ["false"],
    "extrapolateForward": ["true"],
}

MyRecoMCTruthLinker = MarlinProcessorWrapper("MyRecoMCTruthLinker")
MyRecoMCTruthLinker.OutputLevel = INFO
MyRecoMCTruthLinker.ProcessorType = "RecoMCTruthLinker"
MyRecoMCTruthLinker.Parameters = {
    "BremsstrahlungEnergyCut": ["1"],
    "CalohitMCTruthLinkName": ["CalohitMCTruthLink"],
    "ClusterCollection": ["PandoraClusters"],
    "ClusterMCTruthLinkName": ["ClusterMCTruthLink"],
    "FullRecoRelation": ["true"],
    "InvertedNonDestructiveInteractionLogic": ["false"],
    "KeepDaughtersPDG": ["22", "111", "310", "13", "211", "321", "3120"],
    "MCParticleCollection": MCPartColName,
    "MCParticlesSkimmedName": ["MCParticlesSkimmed"],
    "MCTruthClusterLinkName": ["MCTruthClusterLink"],
    "MCTruthRecoLinkName": ["MCTruthRecoLink"],
    "MCTruthTrackLinkName": ["MCTruthSiTracksLink"],
    "RecoMCTruthLinkName": ["RecoMCTruthLink"],
    "RecoParticleCollection": ["PandoraPFOs"],
    "SaveBremsstrahlungPhotons": ["true"],
    "SimCaloHitCollections": [
        "ECalBarrelSiHitsEven",
        "ECalBarrelSiHitsOdd",
        "ECalEndcapSiHitsEven",
        "ECalEndcapSiHitsOdd",
        "HcalBarrelRegCollection",
        "HcalEndcapRingCollection",
        "HcalEndcapsCollection",
        "YokeBarrelCollection",
        "YokeEndcapsCollection",
        "LumiCalCollection",
    ],
    "SimCalorimeterHitRelationNames": ["RelationCaloHit", "RelationMuonHit"],
    "SimTrackerHitCollections": [
        "VertexBarrelCollection",
        "VertexEndcapCollection",
        "InnerTrackerBarrelCollection",
        "InnerTrackerEndcapCollection",
        "TPCCollection",
        "SETCollection",
    ],
    "TrackCollection": ["SiTracks_Refitted"],
    "TrackMCTruthLinkName": ["SiTracksMCTruthLink"],
    "TrackerHitsRelInputCollections": [
        "VertexBarrelTrackerHitRelations",
        "VertexEndcapTrackerHitRelations",
        "InnerTrackerBarrelHitRelations",
        "InnerTrackerEndcapHitRelations",
        "TPCTrackerHitRelations",
        "SETTrackerHitRelations",
    ],
    "UseTrackerHitRelations": ["true"],
    "UsingParticleGun": ["false"],
    "daughtersECutMeV": ["10"],
}


MyTrackChecker = MarlinProcessorWrapper("MyTrackChecker")
MyTrackChecker.OutputLevel = INFO
MyTrackChecker.ProcessorType = "TrackChecker"
MyTrackChecker.Parameters = {
    "MCParticleCollectionName": MCPartColName,
    "TrackCollectionName": ["SiTracks_Refitted"],
    "TrackRelationCollectionName": ["SiTracksMCTruthLink"],
    "TreeName": ["checktree"],
    "UseOnlyTree": ["true"],
}

MyFullLDCTracking_MarlinTrk = MarlinProcessorWrapper("MyFullLDCTracking_MarlinTrk")
MyFullLDCTracking_MarlinTrk.OutputLevel = INFO
MyFullLDCTracking_MarlinTrk.ProcessorType = "FullLDCTracking_MarlinTrk"
MyFullLDCTracking_MarlinTrk.Parameters = {
    "VertexDetectorName": ["VertexBarrel"],
    "AngleCutForForcedMerging": ["0.05"],
    "AngleCutForMerging": ["0.1"],
    "AssignETDHits": ["0"],
    "AssignFTDHits": ["0"],
    "AssignSETHits": ["0"],
    "AssignSITHits": ["0"],
    "AssignTPCHits": ["0"],
    "AssignVTXHits": ["0"],
    "Chi2FitCut": ["100"],
    "CutOnSiHits": ["4"],
    "CutOnTPCHits": ["10"],
    "CutOnTrackD0": ["500"],
    "CutOnTrackZ0": ["500"],
    "D0CutForForcedMerging": ["50"],
    "D0CutForMerging": ["500"],
    "D0CutToMergeTPCSegments": ["100"],
    "Debug": ["0"],
    "DeltaPCutToMergeTPCSegments": ["0.1"],
    "EnergyLossOn": ["true"],
    "FTDHitToTrackDistance": ["2"],
    "FTDPixelHitCollectionName": ["FTDPixelTrackerHits"],
    "FTDSpacePointCollection": ["FTDSpacePoints"],
    "ForbidOverlapInZComb": ["0"],
    "ForbidOverlapInZTPC": ["0"],
    "ForceSiTPCMerging": ["1"],
    "ForceTPCSegmentsMerging": ["0"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.00001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "LDCTrackCollection": ["MarlinTrkTracks"],
    "MaxChi2PerHit": ["200"],
    "MinChi2ProbForSiliconTracks": ["0.00001"],
    "MultipleScatteringOn": ["true"],
    "NHitsExtrapolation": ["35"],
    "OmegaCutForForcedMerging": ["0.15"],
    "OmegaCutForMerging": ["0.25"],
    "PtCutToMergeTPCSegments": ["1.2"],
    "RunMarlinTrkDiagnostics": ["false"],
    "SETHitCollection": ["SETSpacePoints"],
    "SETHitToTrackDistance": ["50"],
    "SITHitCollection": ["InnerTrackerBarrelHits"],
    "SITHitToTrackDistance": ["2"],
    "SiTracks": ["SubsetTracks"],
    "SiTracksMCPRelColl": ["SubsetTracksMCTruthLink"],
    "SmoothOn": ["true"],
    "TPCHitCollection": ["TPCTrackerHits"],
    "TPCHitToTrackDistance": ["15"],
    "TPCTracks": ["ClupatraTracks"],
    "TPCTracksMCPRelColl": ["TPCTracksMCTruthLink"],
    "TrackSystemName": ["DDKalTest"],
    "VTXHitCollection": ["VertexBarrelTrackerHits"],
    "VTXHitToTrackDistance": ["1.5"],
    "Z0CutForForcedMerging": ["200"],
    "Z0CutForMerging": ["1000"],
    "Z0CutToMergeTPCSegments": ["5000"],
    "cosThetaCutHighPtMerge": ["0.99"],
    "cosThetaCutSoftHighPtMerge": ["0.998"],
    "hitDistanceCutHighPtMerge": ["25"],
    "maxFractionOfOutliersCutHighPtMerge": ["0.95"],
    "maxHitDistanceCutHighPtMerge": ["50"],
    "momDiffCutHighPtMerge": ["0.01"],
    "momDiffCutSoftHighPtMerge": ["0.25"],
}


TrackingReco_FCCeeMDISequence = [
    # MyTruthTrackFinder,
    MyClupatraProcessor,
    MyConformalTracking,
    MyFullLDCTracking_MarlinTrk,
    # MyClonesAndSplitTracksFinder,
    # MyRefit,
    # MyRecoMCTruthLinker,
    # MyTrackChecker,
]
