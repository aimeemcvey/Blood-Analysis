def test_HDL_analysis_normal():
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(80)
    expected = "Normal"
    assert answer == expected


def test_HDL_analysis_bl():
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(40)
    expected = "Borderline low"
    assert answer == expected


def test_LDL_analysis_high():
    from chol_analysis import LDL_analysis
    answer = LDL_analysis(165)
    expected = "High"
    assert answer == expected
