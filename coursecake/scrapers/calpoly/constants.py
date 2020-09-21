DEPARTMENTS = [
    "AEPS",
    "AERO",
    "AG",
    "AGB",
    "AGC",
    "AGED",
    "ANT",
    "AP",
    "ARCE",
    "ARCH",
    "ART",
    "ASCI",
    "ASTR",
    "BIO",
    "BMED",
    "BOT",
    "BRAE",
    "BUS",
    "CD",
    "CE",
    "CHEM",
    "CHIN",
    "CLA",
    "CM",
    "CMAT",
    "COMS",
    "CPE",
    "CRP",
    "CSC",
    "CSUC",
    "CSUV",
    "DANC",
    "DATA",
    "DE",
    "DEV10",
    "DSCI",
    "ECON",
    "EDES",
    "EDUC",
    "EE",
    "ENGL",
    "ENGR",
    "ENVE",
    "ERSC",
    "ES",
    "ESCI",
    "EXSS",
    "FPE",
    "FR",
    "FSN",
    "GEOG",
    "GEOL",
    "GER",
    "GRC",
    "GS",
    "GSA",
    "GSB",
    "GSE",
    "GSP",
    "HIST",
    "HLTH",
    "HNRC",
    "HNRS",
    "IME",
    "IP",
    "ISLA",
    "ITAL",
    "ITP",
    "JOUR",
    "JPNS",
    "KINE",
    "LA",
    "LAES",
    "LS",
    "MATE",
    "MATH",
    "MCRO",
    "ME",
    "MSCI",
    "MSL",
    "MU",
    "NE",
    "NR",
    "PEM",
    "PEW",
    "PHIL",
    "PHYS",
    "POLS",
    "PSC",
    "PSY",
    "RELS",
    "RPTA",
    "SCM",
    "SOC",
    "SPAN",
    "SPED",
    "SS",
    "STAT",
    "TH",
    "UNIV",
    "WGS",
    "WLC",
    "WVIT",
]

BASE_URL = "https://cmsweb.pscs.calpoly.edu/psc/CSLOPRD/EMPLOYEE/SA/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL"
BASE_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    # need cookies
    "User-Agent": "User",
    # Set school to CalPoly Slo
}

TERMS_FORM_DATA = {
    "ICAJAX": "1",
    "CLASS_SRCH_WRK2_INSTITUTION$31$": "SLCMP",
    "ICAction": "SLO_SS_DERIVED_STRM$prompt",
}

SEARCH_FORM_DATA = {
    "ICAJAX": "1",
    "CLASS_SRCH_WRK2_INSTITUTION$31$": "SLCMP",
    # Click action is Class Search
    "ICAction": "CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH",
    # Get all classes
    "SSR_CLSRCH_WRK_CATALOG_NBR$1": "99999999",
    "SSR_CLSRCH_WRK_SSR_EXACT_MATCH1$1": "T",
    # Include open AND closed classes
    "SSR_CLSRCH_WRK_SSR_OPEN_ONLY$chk$3": "N",
}

CONFIRM_FORM_DATA = {"ICAction": "#ICSave", "CLASS_SRCH_WRK2_INSTITUTION$31$": "SLCMP"}
