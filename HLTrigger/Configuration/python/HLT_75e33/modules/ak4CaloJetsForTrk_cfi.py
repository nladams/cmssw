import FWCore.ParameterSet.Config as cms

ak4CaloJetsForTrk = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("caloTowerForTrk"),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)
