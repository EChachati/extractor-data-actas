import sqlite3

connection = sqlite3.connect("actas.sqlite")

cursor = connection.cursor()


def create_actas_table():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Acta (
            acta_id VARCHAR(255) PRIMARY KEY,

            PSUV INT,
            PCV INT,
            TUPAMARO INT,
            PPT INT,
            MSV INT,
            PODEMOS INT,
            MEP INT,
            APC INT,
            ORA INT,
            UPV INT,
            EV INT,
            PVV INT,
            PFV INT,
            AD INT,
            COPEI INT,
            MR INT,
            BR INT,
            DDP INT,
            UNE INT,
            EL_CAMBIO INT,
            PV INT,
            VU INT,
            UVV INT,
            MPJ INT,
            AP INT,
            MOVEV INT,
            CMC INT,
            FV INT,
            ALIANZA_DEL_LAPIZ INT,
            MIN_UNIDAD INT,
            SPV INT,
            VPA INT,
            AREPA INT,
            UNTC INT,
            MPV INT,
            MUD INT,
            CENTRADOS INT,
            CONDE INT,

            MADURO_TOTAL INT,
            LUIS_MARTINEZ_TOTAL INT,
            BERTUCCI_TOTAL INT,
            JOSE_BRITO_TOTAL INT,
            ANTONIO_ECARRI_TOTAL INT,
            CLAUDIO_FERMIN_TOTAL INT,
            DANIEL_CEBALLOS_TOTAL INT,
            EDMUNDO_GONZALEZ_TOTAL INT,
            BENJAMIN_RAUSSEO_TOTAL INT,

            TOTAL_VOTES INT,
            TOTAL_NULL INT,
            TOTAL_INVALID INT,

            STATE VARCHAR(255),
            MUNICIPALITY VARCHAR(255),
            PARISH VARCHAR(255),

            image_name VARCHAR(255)
        );
    """
    )
    connection.commit()


def insert_acta_into_db(acta):
    cursor.execute(
        """
            INSERT INTO Acta (
                acta_id,
                PSUV,
                PCV,
                TUPAMARO,
                PPT,
                MSV,
                PODEMOS,
                MEP,
                APC,
                ORA,
                UPV,
                EV,
                PVV,
                PFV,
                AD,
                COPEI,
                MR,
                BR,
                DDP,
                UNE,
                EL_CAMBIO,
                PV,
                VU,
                UVV,
                MPJ,
                AP,
                MOVEV,
                CMC,
                FV,
                ALIANZA_DEL_LAPIZ,
                MIN_UNIDAD,
                SPV,
                VPA,
                AREPA,
                UNTC,
                MPV,
                MUD,
                CENTRADOS,
                CONDE,
                MADURO_TOTAL,
                LUIS_MARTINEZ_TOTAL,
                BERTUCCI_TOTAL,
                JOSE_BRITO_TOTAL,
                ANTONIO_ECARRI_TOTAL,
                CLAUDIO_FERMIN_TOTAL,
                DANIEL_CEBALLOS_TOTAL,
                EDMUNDO_GONZALEZ_TOTAL,
                BENJAMIN_RAUSSEO_TOTAL,
                TOTAL_VOTES,
                TOTAL_NULL,
                TOTAL_INVALID,
                STATE,
                MUNICIPALITY,
                PARISH,
                image_name
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        """,
        (
            acta.acta_id,
            acta.PSUV,
            acta.PCV,
            acta.TUPAMARO,
            acta.PPT,
            acta.MSV,
            acta.PODEMOS,
            acta.MEP,
            acta.APC,
            acta.ORA,
            acta.UPV,
            acta.EV,
            acta.PVV,
            acta.PFV,
            acta.AD,
            acta.COPEI,
            acta.MR,
            acta.BR,
            acta.DDP,
            acta.UNE,
            acta.EL_CAMBIO,
            acta.PV,
            acta.VU,
            acta.UVV,
            acta.MPJ,
            acta.AP,
            acta.MOVEV,
            acta.CMC,
            acta.FV,
            acta.ALIANZA_DEL_LAPIZ,
            acta.MIN_UNIDAD,
            acta.SPV,
            acta.VPA,
            acta.AREPA,
            acta.UNTC,
            acta.MPV,
            acta.MUD,
            acta.CENTRADOS,
            acta.CONDE,
            acta.MADURO_TOTAL,
            acta.LUIS_MARTINEZ_TOTAL,
            acta.BERTUCCI_TOTAL,
            acta.JOSE_BRITO_TOTAL,
            acta.ANTONIO_ECARRI_TOTAL,
            acta.CLAUDIO_FERMIN_TOTAL,
            acta.DANIEL_CEBALLOS_TOTAL,
            acta.EDMUNDO_GONZALEZ_TOTAL,
            acta.BENJAMIN_RAUSSEO_TOTAL,
            acta.TOTAL_VOTES,
            acta.TOTAL_NULL,
            acta.TOTAL_INVALID,
            acta.STATE,
            acta.MUNICIPALITY,
            acta.PARISH,
            acta.image_name,
        ),
    )
    connection.commit()


def is_acta_registered(acta_id):
    cursor.execute("SELECT * FROM Acta WHERE acta_id = ?", (acta_id,))
    return cursor.fetchone() is not None


def is_acta_registered_by_image_name(image_name):
    cursor.execute("SELECT * FROM Acta WHERE  image_name = ?", (image_name,))
    return cursor.fetchone() is not None


def get_all_image_urls(start_id=0):
    cursor.execute("SELECT id, url FROM urls WHERE id > ?", (start_id,))
    return cursor.fetchall()
