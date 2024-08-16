from src.dec_tree.m_classifier import M_Classifier

def test_m_classifier():
    m_classifier = M_Classifier()
    assert m_classifier() < 1.0