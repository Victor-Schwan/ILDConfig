#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper
from Gaudi.Configuration import DEBUG, INFO

CT_MAX_DIST = "0.03;"  # semi-colon is important! RANDOM VALUE COPYIED FROM CLDRECO

MyTruthTrackFinder = MarlinProcessorWrapper("MyTruthTrackFinder")
MyTruthTrackFinder.OutputLevel = DEBUG
MyTruthTrackFinder.ProcessorType = "TruthTrackFinder"
MyTruthTrackFinder.Parameters = {
    "FitForward": ["true"],
    "MCParticleCollectionName": ["MCParticle"],
    "SiTrackCollectionName": ["SiTracksTrue"],
    "SiTrackRelationCollectionName": ["SiTrackRelations"],
    "SimTrackerHitRelCollectionNames": [
        "VertexBarrelTrackerHitRelations ",
        "InnerTrackerBarrelHitRelations",
        "SETTrackerHitRelations",
        "VertexEndcapTrackerHitRelations",
        "InnerTrackerEndcapHitRelations",
    ],
    "TrackerHitCollectionNames": [
        "VertexBarrelTrackerHits",
        "InnerTrackerBarrelHits",
        "SETTrackerHits",
        "VertexEndcapTrackerHits",
        "InnerTrackerEndcapHits",
    ],
    "UseTruthInPrefit": ["false"],
}

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
MyConformalTracking.OutputLevel = INFO
MyConformalTracking.ProcessorType = "ConformalTrackingV2"
MyConformalTracking.Parameters = {
    "DebugHits": ["DebugHits"],
    "DebugPlots": ["false"],
    "DebugTiming": ["false"],
    "MCParticleCollectionName": ["MCParticle"],
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
        "VertexBarrelTrackerHits",
        "VertexEndcapTrackerHits",
        "InnerTrackerBarrelHits",
        "InnerTrackerEndcapHits",
    ],
    "trackPurity": ["0.7"],
    # "Verbosity": ["DEBUG"],
}

# copied from https://github.com/gaswk/CLDConfig/blob/main/CLDConfig/CLDReconstruction.py
MyClonesAndSplitTracksFinder = MarlinProcessorWrapper("MyClonesAndSplitTracksFinder")
MyClonesAndSplitTracksFinder.OutputLevel = DEBUG
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


TrackingReco_FCCeeMDISequence = [
    MyTruthTrackFinder,
    MyClupatraProcessor,
    MyConformalTracking,
    MyClonesAndSplitTracksFinder,
]
