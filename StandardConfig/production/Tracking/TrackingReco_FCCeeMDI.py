#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper
from Gaudi.Configuration import DEBUG, INFO

CT_MAX_DIST = "0.03;"  # semi-colon is important! RANDOM VALUE COPYIED FROM CLDRECO

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
    "VXDHitCollection": ["VXDTrackerHits"],
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
    ],
    "RetryTooManyTracks": ["false"],
    "SiTrackCollectionName": ["SiTracksCT"],
    "SortTreeResults": ["true"],
    # fmt: off
    "Steps": [
        "[VXDBarrel]",
        "@Collections", ":", "VertexBarrelTrackerHits",
        "@Parameters", ":", "MaxCellAngle", ":", "0.01;", "MaxCellAngleRZ", ":", "0.01;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", CT_MAX_DIST, "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;",
        "@Flags", ":", "HighPTFit,", "VertexToTracker",
        "@Functions", ":", "CombineCollections,", "BuildNewTracks",
        # "[VXDEncap]",
        # "@Collections", ":", "VertexEndcapTrackerHits",
        # "@Parameters", ":", "MaxCellAngle", ":", "0.01;", "MaxCellAngleRZ", ":", "0.01;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", CT_MAX_DIST, "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;",
        # "@Flags", ":", "HighPTFit,", "VertexToTracker",
        # "@Functions", ":", "CombineCollections,", "ExtendTracks",
    ],
    # fmt: on
    "ThetaRange": ["0.05"],
    "TooManyTracks": ["100000"],
    "TrackerHitCollectionNames": [
        "VertexBarrelTrackerHits",
        "VertexEndcapTrackerHits",
    ],
    "trackPurity": ["0.7"],
    # "Verbosity": ["DEBUG"],
}


MyTrackSubsetProcessor = MarlinProcessorWrapper("MyTrackSubsetProcessor")
MyTrackSubsetProcessor.OutputLevel = INFO
MyTrackSubsetProcessor.ProcessorType = "TrackSubsetProcessor"
MyTrackSubsetProcessor.Parameters = {
    "EnergyLossOn": ["true"],
    "MultipleScatteringOn": ["true"],
    "Omega": ["0.75"],
    "RemoveShortTracks": ["true"],
    "SmoothOn": ["false"],
    "TrackInputCollections": ["ForwardTracks", "SiTracks"],
    "TrackOutputCollection": ["SubsetTracks"],
    "TrackSystemName": ["DDKalTest"],
}

MyFullLDCTracking_MarlinTrk = MarlinProcessorWrapper("MyFullLDCTracking_MarlinTrk")
MyFullLDCTracking_MarlinTrk.OutputLevel = INFO
MyFullLDCTracking_MarlinTrk.ProcessorType = "FullLDCTracking_MarlinTrk"
MyFullLDCTracking_MarlinTrk.Parameters = {
    "AngleCutForForcedMerging": ["0.05"],
    "AngleCutForMerging": ["0.1"],
    "AssignETDHits": ["0"],
    "AssignFTDHits": ["1"],
    "AssignSETHits": ["1"],
    "AssignSITHits": ["1"],
    "AssignTPCHits": ["0"],
    "AssignVTXHits": ["1"],
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
    "SITHitCollection": ["SITTrackerHits"],
    "SITHitToTrackDistance": ["2"],
    "SiTracks": ["SubsetTracks"],
    "SiTracksMCPRelColl": ["SubsetTracksMCTruthLink"],
    "SmoothOn": ["true"],
    "TPCHitCollection": ["TPCTrackerHits"],
    "TPCHitToTrackDistance": ["15"],
    "TPCTracks": ["ClupatraTracks"],
    "TPCTracksMCPRelColl": ["TPCTracksMCTruthLink"],
    "TrackSystemName": ["DDKalTest"],
    "VTXHitCollection": ["VXDTrackerHits"],
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

MyCompute_dEdxProcessor = MarlinProcessorWrapper("MyCompute_dEdxProcessor")
MyCompute_dEdxProcessor.OutputLevel = INFO
MyCompute_dEdxProcessor.ProcessorType = "Compute_dEdxProcessor"
MyCompute_dEdxProcessor.Parameters = {
    "AngularCorrectionParameters": ["0.635762", "-0.0573237"],
    "EnergyLossErrorTPC": ["0.054"],
    "LDCTrackCollection": ["MarlinTrkTracks"],
    "LowerTruncationFraction": ["0.08"],
    "NumberofHitsCorrectionParameters": ["1.468"],
    "StrategyCompHist": ["false"],
    "StrategyCompHistFiles": ["dEdx_Histo_Strategy"],
    "StrategyCompHistWeight": ["false"],
    "UpperTruncationFraction": ["0.3"],
    "Write_dEdx": ["true"],
    "dEdxErrorScalingExponents": ["-0.34", "-0.45"],
    "dxStrategy": ["1"],
    "isSmearing": ["true"],
    "smearingFactor": [CONSTANTS["dEdXSmearingFactor"]],
}

MyV0Finder = MarlinProcessorWrapper("MyV0Finder")
MyV0Finder.OutputLevel = INFO
MyV0Finder.ProcessorType = "V0Finder"
MyV0Finder.Parameters = {
    "MassRangeGamma": ["0.01"],
    "MassRangeK0S": ["0.02"],
    "MassRangeL0": ["0.02"],
    "TrackCollection": ["MarlinTrkTracks"],
}

MyKinkFinder = MarlinProcessorWrapper("MyKinkFinder")
MyKinkFinder.OutputLevel = INFO
MyKinkFinder.ProcessorType = "KinkFinder"
MyKinkFinder.Parameters = {
    "DebugPrinting": ["0"],
    "TrackCollection": ["MarlinTrkTracks"],
}

MyRefitProcessorKaon = MarlinProcessorWrapper("MyRefitProcessorKaon")
MyRefitProcessorKaon.OutputLevel = INFO
MyRefitProcessorKaon.ProcessorType = "RefitProcessor"
MyRefitProcessorKaon.Parameters = {
    "EnergyLossOn": ["true"],
    "FitDirection": ["-1"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.00001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "InitialTrackState": ["3"],
    "InputTrackCollectionName": ["MarlinTrkTracks"],
    "InputTrackRelCollection": [],
    "OutputTrackCollectionName": ["MarlinTrkTracksKaon"],
    "OutputTrackRelCollection": ["MarlinTrkTracksKaonMCP"],
    "ParticleMass": ["0.493677"],
    "TrackSystemName": ["DDKalTest"],
}

MyRefitProcessorProton = MarlinProcessorWrapper("MyRefitProcessorProton")
MyRefitProcessorProton.OutputLevel = INFO
MyRefitProcessorProton.ProcessorType = "RefitProcessor"
MyRefitProcessorProton.Parameters = {
    "EnergyLossOn": ["true"],
    "FitDirection": ["-1"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.00001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "InitialTrackState": ["3"],
    "InputTrackCollectionName": ["MarlinTrkTracks"],
    "InputTrackRelCollection": [],
    "OutputTrackCollectionName": ["MarlinTrkTracksProton"],
    "OutputTrackRelCollection": ["MarlinTrkTracksProtonMCP"],
    "ParticleMass": ["0.93828"],
    "TrackSystemName": ["DDKalTest"],
}

TrackingReco_FCCeeMDISequence = [
    MyClupatraProcessor,
    MyConformalTracking,
    MyTrackSubsetProcessor,
    MyFullLDCTracking_MarlinTrk,
    MyCompute_dEdxProcessor,
    MyV0Finder,
    # MyKinkFinder,
    MyRefitProcessorKaon,
    MyRefitProcessorProton,
]
