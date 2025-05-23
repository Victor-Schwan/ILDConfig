#!/usr/bin/env python3

# TODO: default names for Collection based on one variable, not individually for REL, HitColl, ...

# non-name parameters of Vertex and Inner D as for CLD (https://github.com/key4hep/CLDConfig/blob/main/CLDConfig/CLDReconstruction.py @ bbb0842)

from Configurables import MarlinProcessorWrapper

VertexBarrelDigitiser = MarlinProcessorWrapper("VertexBarrelDigitiser")
VertexBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VertexBarrelDigitiser.Parameters = {
    "IsStrip": ["false"],
    "ResolutionU": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
    "ResolutionV": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
    "SimTrackHitCollectionName": ["VertexBarrelCollection"],
    "SimTrkHitRelCollection": ["VertexBarrelTrackerHitRelations"],
    "SubDetectorName": ["VertexBarrel"],
    "TrackerHitCollectionName": ["VertexBarrelTrackerHits"],
}

VertexEndcapDigitiser = MarlinProcessorWrapper("VertexEndcapDigitiser")
VertexEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VertexEndcapDigitiser.Parameters = {
    "IsStrip": ["false"],
    "ResolutionU": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
    "ResolutionV": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
    "SimTrackHitCollectionName": ["VertexEndcapCollection"],
    "SimTrkHitRelCollection": ["VertexEndcapTrackerHitRelations"],
    "SubDetectorName": ["VertexEndcap"],
    "TrackerHitCollectionName": ["VertexEndcapTrackerHits"],
}

InnerPlanarDigiProcessor = MarlinProcessorWrapper("InnerPlanarDigiProcessor")
InnerPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerPlanarDigiProcessor.Parameters = {
    "IsStrip": ["false"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.09"],
    "SimTrackHitCollectionName": ["InnerTrackerBarrelCollection"],
    "SimTrkHitRelCollection": ["InnerTrackerBarrelHitRelations"],
    "SubDetectorName": ["InnerTrackerBarrel"],
    "TrackerHitCollectionName": ["InnerTrackerBarrelHits"],
}

InnerEndcapPlanarDigiProcessor = MarlinProcessorWrapper(
    "InnerEndcapPlanarDigiProcessor"
)
InnerEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerEndcapPlanarDigiProcessor.Parameters = {
    "IsStrip": ["false"],
    "ResolutionU": ["0.005", "0.007", "0.007", "0.007", "0.007", "0.007", "0.007"],
    "ResolutionV": ["0.005", "0.09", "0.09", "0.09", "0.09", "0.09", "0.09"],
    "SimTrackHitCollectionName": ["InnerTrackerEndcapCollection"],
    "SimTrkHitRelCollection": ["InnerTrackerEndcapHitRelations"],
    "SubDetectorName": ["InnerTrackerEndcap"],
    "TrackerHitCollectionName": ["InnerTrackerEndcapHits"],
}

SETPlanarDigiProcessor = MarlinProcessorWrapper("SETPlanarDigiProcessor")
SETPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
SETPlanarDigiProcessor.Parameters = {
    "ForceHitsOntoSurface": ["true"],
    "IsStrip": ["true"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0"],
    "SimTrackHitCollectionName": ["SETCollection"],
    "SimTrkHitRelCollection": ["SETTrackerHitRelations"],
    "SubDetectorName": ["SET"],
    "TrackerHitCollectionName": ["SETTrackerHits"],
}

SETDDSpacePointBuilder = MarlinProcessorWrapper("SETDDSpacePointBuilder")
SETDDSpacePointBuilder.ProcessorType = "DDSpacePointBuilder"
SETDDSpacePointBuilder.Parameters = {
    "SimHitSpacePointRelCollection": ["SETSpacePointRelations"],
    "SpacePointsCollection": ["SETSpacePoints"],
    "StripLength": ["9.200000000e+01"],
    "SubDetectorName": ["SET"],
    "TrackerHitCollection": ["SETTrackerHits"],
    "TrackerHitSimHitRelCollection": ["SETTrackerHitRelations"],
}

MyTPCDigiProcessor = MarlinProcessorWrapper("MyTPCDigiProcessor")
MyTPCDigiProcessor.ProcessorType = "DDTPCDigiProcessor"
MyTPCDigiProcessor.Parameters = {
    "DiffusionCoeffRPhi": ["0.025"],
    "DiffusionCoeffZ": ["0.08"],
    "DoubleHitResolutionRPhi": ["2"],
    "DoubleHitResolutionZ": ["5"],
    "HitSortingBinningRPhi": ["2"],
    "HitSortingBinningZ": ["5"],
    "MaxClusterSizeForMerge": ["3"],
    "N_eff": ["22"],
    "PointResolutionPadPhi": ["0.9"],
    "PointResolutionRPhi": ["0.05"],
    "PointResolutionZ": ["0.4"],
    "RejectCellID0": ["1"],
    "SimTrkHitRelCollection": ["TPCTrackerHitRelations"],
    "TPCEndPlateModuleGapPhi": ["1."],
    "TPCEndPlateModuleGapR": ["1."],
    "TPCEndPlateModuleNumbers": ["14", "18", "23", "28", "32", "37", "42", "46"],
    "TPCEndPlateModulePhi0s": [
        "0",
        "0.17453292519943298",
        "0.030350516853376176",
        "0.2108457469509264",
        "0.11998920441304516",
        "0.1600004647682326",
        "0.02051011203843622",
        "0.062176216344090166",
    ],
    "TPCLowPtCollectionName": ["TPCLowPtCollection"],
    "TPCPadRowHitCollectionName": ["TPCCollection"],
    "TPCSpacePointCollectionName": ["TPCSpacePointCollection"],
    "TPCTrackerHitsCol": ["TPCTrackerHits"],
}

TrackingDigi_FCCeeMDISequence = [
    VertexEndcapDigitiser,
    VertexBarrelDigitiser,
    InnerPlanarDigiProcessor,
    InnerEndcapPlanarDigiProcessor,
    SETPlanarDigiProcessor,
    SETDDSpacePointBuilder,
    MyTPCDigiProcessor,
]
