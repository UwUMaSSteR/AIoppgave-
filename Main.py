from database import init_db, save_version, get_last_version
from vlc_cheker import get_latest_vlc_version

def main():
    init_db()

    print("sjeker siste verson vlc")

    latest = get_latest_vlc_version()

    if not latest:
        print("fikk ikke informasjon om verson.")
        return

    last_saved = get_last_version()

    print("siste mulig verson:", latest)

    if last_saved is None:
        print("Det finnes ingen tidligere data i databasen. Vi lagrer den nåværende versjonen..")
        save_version(latest)

    elif latest != last_saved:
        print("NY VERSJON FUNNET!")
        print("Tidligere:", last_saved)
        print("Ny:", latest)
        save_version(latest)

    else:
        print("Du har allerede lagret den nyeste versjonen.")

if __name__ == "__main__":
    main()
