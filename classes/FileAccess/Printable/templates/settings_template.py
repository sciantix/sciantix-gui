
"""
----------------------------------------------------------------------------------------------------------------------------------
     _______.  ______  __      ___     .__   __..___________.|| __           __  __  __________      ___     ._______ ._____
    /       | /      ||  |    /   \    |  \ |  ||           |//\  \         /  /|  ||______    |    /   \    |   _   \|  _  \
   |   (----`|  ,----'|  |   /  ^  \   |   \|  |`---|  |----`   \  \   ^   /  / |  |     _/  _/    /  ^  \   |  |_)  || | \  \
    \   \    |  |     |  |  /  /_\  \  |  . `  |    |  |         \  \ / \ /  /  |  |   _/  _/     /  /_\  \  |   ____/| |  )  |
.----)   |   |  `----.|  | /  _____  \ |  |\   |    |  |          \  v   v  /   |  | _/  _/____  /  _____  \ |  |\  \ | |_/  /
|_______/     \______||__|/__/     \__\|__| \__|    |__|           \__/^\__/    |__||__________|/__/     \__\|__| \__\|_____/

----------------------------------------------------------------------------------------------------------------------------------

    Originally developed by G. Léandre

    Version : 1.4.3
    Year :    2026
    Authors : G. Léandre
"""


def template(input_file_class):
    file_content = str()
    i            = 0

    comments = [
        r"iGrainGrowth (0= no grain growth, 1= Ainscough et al. (1973), 2= Van Uffelen et al. (2013))",
        r"iFissionGasDiffusivity (0= constant value, 1= Turnbull et al. (1988))",
        r"iDiffusionSolver (1= SDA with quasi-stationary hypothesis, 2= SDA without quasi-stationary hypothesis)",
        r"iIntraGranularBubbleBehavior (1= Pizzocri et al. (2018))",
        r"iResolutionRate (0= constant value, 1= Turnbull (1971), 2= Losonen (2000), 3= thermal resolution, Cognini et al. (2021))",
        r"iTrappingRate (0= constant value, 1= Ham (1958))",
        r"iNucleationRate (0= constant value, 1= Olander, Wongsawaeng (2006))",
        r"iOutput (1= default output files)",
        r"iGrainBoundaryVacancyDiffusivity (0= constant value, 1= Reynolds and Burton (1979), 2= White (2004))",
        r"iGrainBoundaryBehaviour (0= no grain boundary bubbles, 1= Pastore et al (2013))",
        r"iGrainBoundaryMicroCracking (0= no model considered, 1= Barani et al. (2017))",
        r"iFuelMatrix (0= UO2, 1= UO2 + HBS)",
        r"iGrainBoundaryVenting (0= no model considered, 1= Pizzocri et al., D6.4 (2020), H2020 Project INSPYRE)",
        r"iRadioactiveFissionGas (0= not considered)",
        r"iHelium (0= not considered)",
        r"iHeDiffusivity (0= null value, 1= limited lattice damage, Luzzi et al. (2018), 2= significant lattice damage, Luzzi et al. (2018))",
        r"iGrainBoundarySweeping (0= no model considered, 1= TRANSURANUS swept volume model)",
        r"iHighBurnupStructureFormation (0= no model considered, 1= fraction of HBS-restructured volume from Barani et al. (2020))",
        r"iHighBurnupStructurePorosity (0= no evolution of HBS porosity, 1= HBS porosity evolution based on Spino et al. (2006) data)",
        r"iHeliumProductionRate (0= zero production rate, 1= helium from ternary fissions, 2= linear with burnup (FR))",
        r"iStoichiometryDeviation (0= not considered, 1= Cox et al. 1986, 2= Bittel et al. 1969, 3= Abrefah et al. 1994, 4= Imamura et al. 1997, 5= Langmuir-based approach)",
        r"iBubbleDiffusivity (0= not considered, 1= volume diffusivity)",
        r"iDensification (0= not considered, 1= P. Van Uffelen PhD thesis (2002))",
    ]


    for name in input_file_class.getOptionsNames():
        file_content += f"{input_file_class.getValueByName(name)}\t#\t{comments[i]}\n"
        i += 1

    return file_content
