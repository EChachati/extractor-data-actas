from dataclasses import dataclass

from static_data import (
    ANTONIO_ECARRI_PARTIES,
    BENJAMIN_RAUSSEO_PARTIES,
    BERTUCCI_PARTIES,
    CLAUDIO_FERMIN_PARTIES,
    DANIEL_CEBALLOS_PARTIES,
    EDMUNDO_GONZALEZ_PARTIES,
    JOSE_BRITO_PARTIES,
    LUIS_MARTINEZ_PARTIES,
    MADURO_PARTIES,
    PARTIES,
)


@dataclass
class Acta:
    acta_id: str

    PSUV: int
    PCV: int
    TUPAMARO: int
    PPT: int
    MSV: int
    PODEMOS: int
    MEP: int
    APC: int
    ORA: int
    UPV: int
    EV: int
    PVV: int
    PFV: int
    AD: int
    COPEI: int
    MR: int
    BR: int
    DDP: int
    UNE: int
    EL_CAMBIO: int
    PV: int
    VU: int
    UVV: int
    MPJ: int
    AP: int
    MOVEV: int
    CMC: int
    FV: int
    ALIANZA_DEL_LAPIZ: int
    MIN_UNIDAD: int
    SPV: int
    VPA: int
    AREPA: int
    UNTC: int
    MPV: int
    MUD: int
    CENTRADOS: int
    CONDE: int

    MADURO_TOTAL: int
    LUIS_MARTINEZ_TOTAL: int
    BERTUCCI_TOTAL: int
    JOSE_BRITO_TOTAL: int
    ANTONIO_ECARRI_TOTAL: int
    CLAUDIO_FERMIN_TOTAL: int
    DANIEL_CEBALLOS_TOTAL: int
    EDMUNDO_GONZALEZ_TOTAL: int
    BENJAMIN_RAUSSEO_TOTAL: int

    TOTAL_VOTES: int
    TOTAL_NULL: int
    TOTAL_INVALID: int

    STATE: str
    MUNICIPALITY: str
    PARISH: str

    image_name: str

    def __init__(self, acta_id, **kwargs):
        self.acta_id = acta_id
        for party, votes in kwargs.items():
            setattr(self, party, votes)

        self.MADURO_TOTAL = sum([getattr(self, party) for party in MADURO_PARTIES])
        self.LUIS_MARTINEZ_TOTAL = sum([getattr(self, party) for party in LUIS_MARTINEZ_PARTIES])
        self.BERTUCCI_TOTAL = sum([getattr(self, party) for party in BERTUCCI_PARTIES])
        self.JOSE_BRITO_TOTAL = sum([getattr(self, party) for party in JOSE_BRITO_PARTIES])
        self.ANTONIO_ECARRI_TOTAL = sum([getattr(self, party) for party in ANTONIO_ECARRI_PARTIES])
        self.CLAUDIO_FERMIN_TOTAL = sum([getattr(self, party) for party in CLAUDIO_FERMIN_PARTIES])
        self.DANIEL_CEBALLOS_TOTAL = sum(
            [getattr(self, party) for party in DANIEL_CEBALLOS_PARTIES]
        )
        self.EDMUNDO_GONZALEZ_TOTAL = sum(
            [getattr(self, party) for party in EDMUNDO_GONZALEZ_PARTIES]
        )
        self.BENJAMIN_RAUSSEO_TOTAL = sum(
            [getattr(self, party) for party in BENJAMIN_RAUSSEO_PARTIES]
        )

        self.TOTAL_VOTES = sum([getattr(self, party) for party in PARTIES])

    def __str__(self):
        return f"""
        Acta {self.acta_id}
        Image: {self.image_name}
        State: {self.STATE}
        Municipality: {self.MUNICIPALITY}
        Parish: {self.PARISH}

        MADURO: {self.MADURO_TOTAL}
        LUIS MARTINEZ: {self.LUIS_MARTINEZ_TOTAL}
        BERTUCCI: {self.BERTUCCI_TOTAL}
        JOSE BRITO: {self.JOSE_BRITO_TOTAL}
        ANTONIO ECARRI: {self.ANTONIO_ECARRI_TOTAL}
        CLAUDIO FERMIN: {self.CLAUDIO_FERMIN_TOTAL}
        DANIEL CEBALLOS: {self.DANIEL_CEBALLOS_TOTAL}
        EDMUNDO GONZALEZ: {self.EDMUNDO_GONZALEZ_TOTAL}
        BENJAMIN RAUSSEO: {self.BENJAMIN_RAUSSEO_TOTAL}

        """
