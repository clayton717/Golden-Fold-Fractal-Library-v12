# Golden Fold Quantum Media Companion v12 - Infinite Fractal Library
# © 2025 Clayton Alexander McKinney. All rights reserved.
# Formula: Abstraction through fractal application equals reality.
# Formula established: Feb 19th, 2025, 8:20 P.M. PST
# Version: v12 - Infinite Fractal Library
# SHA256: [9c53ab60d383a3bc044ae70f1a13f675e5f564df5b86f9d8a8ff55ee27fb9753]
# Device: Optimized for Pydroid3 on Samsung Galaxy S9 (Android)
# This is CHUNK 1 of N. Paste CHUNK 2 directly below to continue.

import webbrowser, datetime, hashlib, random, sys, os, zipfile, json

# --- CORE METADATA & CONSTANTS ---
FAVORITES_FILE = "golden_fold_favorites.txt"
NOTES_FILE = "golden_fold_notes.txt"
LOG_FILE = "golden_fold_media_log.txt"
USER_SCORES_FILE = "golden_fold_user_scores.json"
USER_PROFILES_FILE = "golden_fold_user_profiles.json"

MEDIA_COMPANION_FORMULA = "Abstraction through fractal application equals reality."
MEDIA_COMPANION_FORMULA_DATE = "Feb 19th, 2025, 8:20 P.M. PST"
MEDIA_COMPANION_VERSION = "v12 - Infinite Fractal Library"
MEDIA_COMPANION_TIMESTAMP = datetime.datetime.now().strftime("%A, %B %d, %Y, %I:%M %p")
MEDIA_COMPANION_AUTHOR = "Clayton Alexander McKinney"
MEDIA_COMPANION_DEVICE = "Pydroid3 / Galaxy S9"

# --- SHA256 HASHING ---
def sha256_file(filepath):
    try:
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception as e:
        return f"SHA256 Error: {e}"

def digital_watermark(text):
    stamp = f"{MEDIA_COMPANION_FORMULA}|{MEDIA_COMPANION_AUTHOR}|{MEDIA_COMPANION_FORMULA_DATE}"
    return f"{text}\n-- {stamp} --"

# --- PACKAGING (EXPORT/IMPORT) ---
def export_logs():
    files = [LOG_FILE, FAVORITES_FILE, NOTES_FILE, USER_SCORES_FILE, USER_PROFILES_FILE]
    zlist = [f for f in files if os.path.isfile(f)]
    if not zlist:
        print("No logs to export.")
        return
    zipname = f"GFMediaBundle_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    with zipfile.ZipFile(zipname, "w") as zipf:
        for f in zlist:
            zipf.write(f)
    print(f"Archived to {zipname} for backup/share! SHA256: {sha256_file(zipname)}")

def import_logs():
    print("Paste the path to your exported ZIP (or 0 to back):")
    path = input("> ").strip()
    if path == "0":
        return
    if not os.path.isfile(path):
        print("File not found.")
        return
    try:
        with zipfile.ZipFile(path, "r") as zipf:
            zipf.extractall()
        print("Import complete.")
    except Exception as e:
        print("Import failed:", e)

# --- SUPER-EXPANDED, MERGED MEDIA LIBRARY (ALL CATEGORIES) ---
MEDIA_LIB = {
    "Books, Literature & Research": [
        ("Project Gutenberg", "https://gutenberg.org/", "70,000+ classic & public domain eBooks"),
        ("Open Library", "https://openlibrary.org/", "Global book database & digital lending"),
        ("HathiTrust Digital Library", "https://www.hathitrust.org/", "18M+ digitized scholarly works"),
        ("Gallica (BnF)", "https://gallica.bnf.fr/", "9M+ books, manuscripts, images, music"),
        ("World Digital Library", "https://www.wdl.org/", "UNESCO global library: rare books, maps, archives"),
        ("Digital Bodleian", "https://digital.bodleian.ox.ac.uk/", "Oxford’s digitized manuscripts, books"),
        ("Project Runeberg", "https://runeberg.org/", "Digitized Nordic literature, classics & poems"),
        ("Digital Walters", "https://www.thedigitalwalters.org/", "High-res, annotated medieval manuscripts"),
        ("OpenStax", "https://openstax.org/", "Peer-reviewed, open-access college textbooks"),
        ("Open Textbook Library", "https://open.umn.edu/opentextbooks", "K-12 and college OER textbooks"),
        ("Directory of Open Access Books", "https://www.doabooks.org/", "80,000+ peer-reviewed OA books"),
        ("MERLOT", "https://www.merlot.org/", "Free, peer-reviewed teaching/learning materials"),
        ("OER Commons", "https://www.oercommons.org/", "Global OER: lesson plans, textbooks, tools"),
        ("Project MUSE OA Books", "https://muse.jhu.edu/browse?f=open_access", "OA scholarly books"),
        ("Digital Commonwealth", "https://www.digitalcommonwealth.org/", "700,000+ digitized books, images, audio"),
        ("South Asian Digital Heritage", "http://sadbhavna.org.in/", "South Asian manuscripts, oral literature"),
        ("ProQuest Digital Collections", "https://about.proquest.com/en/", "160M+ books, journals, video, audio"),
        ("California Digital Library", "https://cdlib.org/", "UC system-wide digital library"),
        ("CloudLibrary", "https://www.yourcloudlibrary.com/", "Millions of ebooks/audiobooks/magazines"),
        ("LibraryWorld", "https://www.libraryworld.com/", "Modern ILS, open access catalog"),
        ("WikiLibrary", "https://wikilibrary.org/", "Open, collaborative library catalog"),
        ("Mandarin M5", "https://www.mlasolutions.com/", "Mobile-responsive public catalog"),
        ("OPALS", "https://www.opalsinfo.net/", "1,000+ libraries, open source ILS"),
        ("Media Flex OPALS", "https://www.mediaflex.net/", "Hosted, open source ILS"),
        ("OCLC WorldCat", "https://www.worldcat.org/", "Global union catalog"),
        ("Internet Archive Books", "https://archive.org/details/texts", "All scanned content"),
        ("Europeana Books & Manuscripts", "https://www.europeana.eu/en/collections/topic/18-books-and-manuscripts", "Pan-European books, manuscripts"),
    ],
    "News, Periodicals & Magazines": [
        ("Chronicling America", "https://chroniclingamerica.loc.gov/", "Historic US Newspapers, 18th–20th c."),
        ("Trove Newspapers", "https://trove.nla.gov.au/newspaper/", "Australian historic/regional newspapers"),
        ("Europeana Newspapers", "https://www.europeana.eu/en/collections/topic/18-newspapers", "Multi-language European papers"),
        ("British Newspaper Archive", "https://www.britishnewspaperarchive.co.uk/", "Historic UK press (some OA)"),
        ("Google News Archive", "https://news.google.com/newspapers", "Historic global newspapers"),
        ("Elephind", "https://www.elephind.com/", "Meta-search: world libraries & newspapers"),
        ("Historical Jewish Press", "https://www.jpress.org.il/", "Jewish newspapers worldwide"),
        ("Hemeroteca Digital Brasileira", "https://bndigital.bn.gov.br/hemeroteca-digital/", "Brazilian magazines/newspapers"),
        ("PERSÉE", "https://www.persee.fr/", "French OA periodicals"),
        ("ProQuest Digital Collections", "https://about.proquest.com/en/", "Journals, periodicals, magazines"),
        ("CloudLibrary", "https://www.yourcloudlibrary.com/", "Digital newspapers, magazines"),
        ("OCLC WorldCat Periodicals", "https://www.worldcat.org/", "Global periodicals"),
        ("California Digital Library", "https://cdlib.org/", "UC system-wide digital library"),
    ],
    "Art, Photography, VR & 3D": [
        ("Smithsonian Open Access", "https://www.si.edu/OpenAccess", "4.5M+ museum objects, CC0"),
        ("The Met Open Access", "https://www.metmuseum.org/art/collection", "400k+ open artworks"),
        ("Getty Open Content", "https://www.getty.edu/opencontent/", "100,000+ images, global art/photo"),
        ("MoMA Open Artworks", "https://www.moma.org/collection/works", "Modern/contemporary art"),
        ("Europeana Art", "https://www.europeana.eu/en/collections/topic/13-art", "European art, all eras"),
        ("WikiArt", "https://www.wikiart.org/", "250,000+ artworks, global"),
        ("Rijksmuseum Open", "https://www.rijksmuseum.nl/en/rijksstudio", "Dutch art, 700k+ images"),
        ("Wellcome Collection", "https://wellcomecollection.org/works?query=image", "Medical/cultural/science images"),
        ("Flickr Commons", "https://www.flickr.com/commons", "Museum/institutional photo archives"),
        ("Sketchfab Free 3D", "https://sketchfab.com/features/free-3d-models", "3D models/environments for VR"),
        ("Smithsonian 3D", "https://3d.si.edu/collections", "Museum 3D models for VR/AR"),
        ("Mozilla Hubs Public Rooms", "https://hubs.mozilla.com/explore", "Social VR with open-access worlds"),
        ("Viveport Indie/Free", "https://www.viveport.com/", "Indie/experimental VR"),
        ("VRChat Worlds Directory", "https://vrchat.com/home/worlds", "User-created VRChat open worlds"),
        ("Within VR", "https://www.within.com/", "VR documentaries/narrative"),
        ("Library of Congress Digital Collections", "https://www.loc.gov/collections/", "Photos, maps, VR, digital adventures"),
        ("ProQuest Digital Collections", "https://about.proquest.com/en/", "Visual arts, design"),
        ("CloudLibrary", "https://www.yourcloudlibrary.com/", "Art/photography ebooks/media"),
    ],
    # ... (continue with all other super-categories in same format, see next chunk)
}

# --- END OF CHUNK 1 ---
# Next: CHUNK 2 will continue the MEDIA_LIB with all remaining super-categories, then add navigation, search, AI, and user features.
# Paste CHUNK 2 directly below this comment to continue.
# --- CHUNK 2: CONTINUE MEDIA_LIB SUPER-CATEGORIES ---

MEDIA_LIB.update({
    "Music, Audio, Sound & Podcasts": [
        ("Free Music Archive", "https://freemusicarchive.org/", "Open/CC music, all genres"),
        ("Internet Archive 78rpm", "https://archive.org/details/georgeblood", "400k+ digitized historic music records"),
        ("British Library Sounds", "https://sounds.bl.uk/", "Field/folk/wildlife/oral history, 95,000+ tracks"),
        ("Smithsonian Folkways", "https://folkways.si.edu/", "Global music and oral history"),
        ("Freesound", "https://freesound.org/", "CC-licensed sound samples and FX"),
        ("Radiooooo", "https://radiooooo.com/", "Musical time travel by country/decade"),
        ("Open Music Archive", "https://openmusicarchive.org/", "Music, global, all genres"),
        ("Global Jukebox", "https://theglobaljukebox.org/", "Folk music from every continent, mapped"),
        ("Podcast Archive", "https://archive.org/details/podcasts", "Podcasts, all genres"),
        ("BBC Public Domain Radio", "https://www.bbcrewind.co.uk/", "Historic, radio"),
        ("Europeana Music", "https://www.europeana.eu/en/collections/topic/16-music", "European music, all eras"),
        ("ProQuest Digital Collections", "https://about.proquest.com/en/", "15M+ audio tracks, music, oral history"),
        ("CloudLibrary", "https://www.yourcloudlibrary.com/", "Audiobooks, music, podcasts"),
        ("California Digital Library", "https://cdlib.org/", "UC system-wide digital library"),
    ],
    "Movies, TV, Streaming & Animation": [
        ("Internet Archive Feature Films", "https://archive.org/details/feature_films", "Public domain and open movies from all eras"),
        ("Open Culture Free Movies", "https://www.openculture.com/freemoviesonline", "Curated free/PD/indie films"),
        ("Kanopy", "https://www.kanopy.com/", "Modern/Indie/Classic (library card required)"),
        ("BFI Player Free", "https://player.bfi.org.uk/free", "UK film and documentary streaming"),
        ("NFB Canada", "https://www.nfb.ca/", "Award-winning Canadian docs and animation"),
        ("Asian Film Archive", "https://www.asianfilmarchive.org/", "Southeast Asian historic cinema"),
        ("Criterion Channel Free", "https://www.criterionchannel.com/browse", "Classic/art films (free section)"),
        ("Prelinger Archives", "https://archive.org/details/prelinger", "Historic ephemeral films, US/ads/education"),
        ("European Film Gateway", "http://www.europeanfilmgateway.eu/", "Pan-European film heritage"),
        ("Classic Cinema Online", "http://www.classiccinemaonline.com/", "Classic, 1920s-50s"),
        ("Midnight Movie Archive", "http://midnight-movie.com/", "Cult classic and horror movies"),
        ("JustWatch Public Domain Movies", "https://www.justwatch.com/us/provider/public-domain", "Public domain streaming movies"),
        ("Public Domain Day 2025", "https://web.law.duke.edu/cspd/publicdomainday/2025/", "Newly public domain films and media"),
        ("Internet Archive Classic TV", "https://archive.org/details/classic_tv", "Classic TV, all genres"),
        ("Animation Archive", "https://archive.org/details/classicanimation", "Classic animation/cartoons"),
        ("RetroCrush Anime", "https://retrocrush.tv/", "Classic anime, free/ad-supported"),
        ("Open Culture Free TV", "https://www.openculture.com/freetvshows", "Curated classic/indie TV"),
        ("Museum of Classic Chicago TV", "https://www.fuzzymemories.tv/", "Thousands of local TV, news, kids’ shows"),
        ("Dust Sci-Fi", "https://www.youtube.com/c/watchdust", "Indie sci-fi shorts/series"),
        ("OpenTV Beta", "https://weareopen.tv/", "Queer & BIPOC web series"),
        ("American Archive of Public Broadcasting", "https://americanarchive.org/", "PBS and local US public TV/radio"),
        ("Open Video Project", "http://www.open-video.org/", "Educational/documentary TV"),
        ("British Pathé", "https://www.youtube.com/user/britishpathe", "Newsreels and historic footage"),
        ("Vimeo Staff Picks", "https://vimeo.com/channels/staffpicks", "Indie/experimental web video"),
        ("ProQuest Digital Collections", "https://about.proquest.com/en/", "24,000+ video titles, film, TV, streaming"),
        ("CloudLibrary", "https://www.yourcloudlibrary.com/", "Streaming video"),
        ("Hoopla", "https://www.hoopladigital.com/", "Public library streaming movies/TV"),
        ("OverDrive Video", "https://www.overdrive.com/", "Public library streaming video"),
        ("OCLC WorldCat Video", "https://www.worldcat.org/", "Global video catalog"),
        ("California Digital Library", "https://cdlib.org/", "UC system-wide digital library"),
    ],
    "Games, Interactive & Tabletop": [
        ("Internet Archive Console Living Room", "https://archive.org/details/consolelivingroom", "In-browser retro console/PC games"),
        ("ClassicReload.com", "https://classicreload.com/", "DOS, PC, and arcade classics"),
        ("Abandonia", "https://www.abandonia.com/", "Abandonware DOS games"),
        ("Home of the Underdogs", "https://homeoftheunderdogs.net/", "Legendary freeware/shareware PC classics"),
        ("itch.io Free/Open", "https://itch.io/games/free", "Indie games, open/CC"),
        ("Game Jolt Free", "https://gamejolt.com/games/free", "Free indie game community"),
        ("Interactive Fiction Archive", "http://www.ifarchive.org/", "Text adventures/interactive fiction"),
        ("Internet Archive Arcade", "https://archive.org/details/internetarcade", "Classic arcade games"),
        ("BoardGameGeek Print & Play", "https://boardgamegeek.com/boardgamecategory/print-play", "Open printable board games"),
        ("PICO-8 BBS", "https://www.lexaloffle.com/bbs/", "Play/fork fantasy console games"),
        ("OpenGameArt.org", "https://opengameart.org/", "Open sprites/assets, some games playable"),
        ("DriveThruRPG Open", "https://www.drivethrurpg.com/browse/pub/48/Open-Game-License", "Free & open roleplaying games"),
        ("OpenAbandonware Games", "https://www.openabandonware.com/", "Open and classic abandonware games"),
        ("Libregamewiki", "https://libregamewiki.org/", "Free/libre open source games"),
        ("Classic PC Games", "https://classicpcgames.com/", "Classic PC games, DOS/Windows"),
        ("My Abandonware", "https://www.myabandonware.com/", "Thousands of old games to download/play"),
        ("ProQuest Digital Collections", "https://about.proquest.com/en/", "Entertainment/games (where available)"),
        ("CloudLibrary", "https://www.yourcloudlibrary.com/", "Interactive ebooks/games"),
    ],
    "Comics, Manga & Graphic Novels": [
        ("Internet Archive Anime Collection", "https://archive.org/details/anime", "Public domain/fan-translated anime"),
        ("RetroCrush Anime", "https://retrocrush.tv/", "Classic anime, free/ad-supported"),
        ("Open Culture Free Anime", "https://www.openculture.com/freemoviesonline", "Curated anime links"),
        ("MangaZ", "https://mangaz.com/", "Open manga scans, translations"),
        ("Digital Comic Museum", "https://digitalcomicmuseum.com/", "Golden/Silver Age comics, some manga"),
        ("Comic Book Plus", "https://comicbookplus.com/", "Public domain comics & manga"),
        ("Europeana Comics", "https://www.europeana.eu/en/collections/topic/72-comics", "Global/EU open comics"),
        ("Mangapark", "https://mangapark.net/", "Open/translated manga reader"),
        ("CloudLibrary", "https://www.yourcloudlibrary.com/", "Digital comics, graphic novels"),
        ("ProQuest Digital Collections", "https://about.proquest.com/en/", "Comics/graphic novels"),
        ("OpenComic", "https://opencomic.org/", "Open source comic reader and library"),
        ("ComicFury", "https://comicfury.com/", "Webcomic hosting and discovery"),
        ("Webtoon", "https://www.webtoons.com/", "Webcomics and manga (free section)"),
    ],
    "Science, Education & Open Data": [
        ("arXiv", "https://arxiv.org/", "2.5M+ preprints (physics, math, CS, etc.)"),
        ("PubMed Central", "https://www.ncbi.nlm.nih.gov/pmc/", "OA biomedical/life science research"),
        ("CORE", "https://core.ac.uk/", "280M+ OA research papers, global"),
        ("DOAJ", "https://doaj.org/", "20,000+ peer-reviewed OA journals"),
        ("OpenStax", "https://openstax.org/", "Free open textbooks and learning materials"),
        ("Zenodo", "https://zenodo.org/", "OA datasets, publications, software"),
        ("Europeana Science", "https://www.europeana.eu/en/collections/topic/58-science", "Science images & artifacts, global"),
        ("Biodiversity Heritage Library", "https://www.biodiversitylibrary.org/", "Historic biodiversity science books/data"),
        ("NASA Open Data Portal", "https://data.nasa.gov/", "Open earth/space datasets"),
        ("ScopusAI", "https://www.scopus.com/", "AI-powered academic search"),
        ("ProQuest Digital Collections", "https://about.proquest.com/en/", "Science, STEM, data, OA journals"),
        ("California Digital Library", "https://cdlib.org/", "UC system-wide digital library"),
        ("CloudLibrary", "https://www.yourcloudlibrary.com/", "STEM ebooks, educational media"),
        ("OpenAIRE", "https://www.openaire.eu/", "European open science infrastructure"),
        ("Open Science Framework", "https://osf.io/", "Open research, data, and preprints"),
    ],
    "Special Media, Ephemera & Meta-portals": [
        ("Public Domain Review", "https://publicdomainreview.org/", "Curated rare/ephemeral/forgotten works"),
        ("Internet Archive Ephemera", "https://archive.org/details/ephemera", "Posters, flyers, paper ephemera"),
        ("OpenGLAM", "http://openglam.org/", "Open galleries, libraries, archives, museums"),
        ("Wikimedia Commons", "https://commons.wikimedia.org/", "99M+ open images, video, sound"),
        ("Open Knowledge Maps", "https://openknowledgemaps.org/", "Visual search of open research"),
        ("Atlas Obscura Open Guides", "https://www.atlasobscura.com/things-to-do", "Unusual places, guides, and secrets"),
        ("Computers in Libraries Innovation Showcases", "https://computersinlibraries.infotoday.com/", "Cutting-edge digital library tech"),
        ("Library of Congress Digital Adventures", "https://www.loc.gov/collections/digital-adventures/", "Interactive, educational digital experiences"),
        ("ProQuest Digital Collections", "https://about.proquest.com/en/", "Archival, rare, and meta-content"),
        ("CloudLibrary", "https://www.yourcloudlibrary.com/", "Ephemera, rare items"),
    ],
    "World Culture, Language & Folklore": [
        ("South Asian Digital Heritage", "http://sadbhavna.org.in/", "South Asian regional manuscripts, oral literature, and classics"),
        ("World Digital Library", "https://www.wdl.org/", "Global rare books, folklore, maps"),
        ("Digital Himalaya", "https://digitalhimalaya.com/", "Tibetan and Himalayan cultural recordings and texts"),
        ("StoryCorps Archive", "https://archive.storycorps.org/", "Thousands of recorded personal stories"),
        ("World Oral Literature Project", "https://www.oralliterature.org/", "Indigenous storytelling traditions"),
        ("Smithsonian Folkways", "https://folkways.si.edu/", "Global folk music and oral histories"),
        ("ProQuest Digital Collections", "https://about.proquest.com/en/", "Anthropology, global studies, international relations"),
        ("ProQuest One", "https://about.proquest.com/en/products-services/proquest-one-academic/", "Global culture disciplines"),
        ("CloudLibrary", "https://www.yourcloudlibrary.com/", "Language learning, world culture ebooks/media"),
        ("Europeana World Cultures", "https://www.europeana.eu/en/collections/topic/20-world-cultures", "Pan-European world culture collections"),
        ("Endangered Languages Project", "https://www.endangeredlanguages.com/", "Preservation of the world's languages"),
        ("Ethnologue", "https://www.ethnologue.com/", "Comprehensive reference of world languages"),
        ("Open Language Archives Community", "http://www.language-archives.org/", "Open resources for language documentation"),
    ],
    "AI Tools & Digital Library Tech": [
        ("ScopusAI", "https://www.scopus.com/", "AI-powered academic search and evaluation"),
        ("ProQuest Research Assistant", "https://about.proquest.com/en/", "AI-powered research tools"),
        ("LibraryWorld Kids Catalog", "https://www.libraryworld.com/", "Discovery tools for young users"),
        ("Computers in Libraries Innovation Showcases", "https://computersinlibraries.infotoday.com/", "Library tech and AI showcases"),
        ("Mandarin M5 mobile interface", "https://www.mlasolutions.com/", "Mobile-optimized library catalog"),
        ("OPALS AI features", "https://www.opalsinfo.net/", "AI tools for school/public libraries"),
        ("OCLC WorldCat Discovery AI", "https://www.worldcat.org/discovery", "AI-enhanced global catalog search"),
        ("OpenAI Datasets", "https://openai.com/datasets", "Open datasets for AI research"),
        ("OpenML", "https://www.openml.org/", "Open machine learning datasets and tools"),
    ]
})

# --- END OF CHUNK 2 ---
# Next: CHUNK 3 will add seamless navigation, smart search, trending, AI-powered suggestions, user profiles, and all expert features.
# Paste CHUNK 3 directly below this comment to continue.
# --- CHUNK 3: NAVIGATION, SEARCH, FAVORITES, NOTES, TRENDING, SESSION ---

def list_categories():
    print("\nCategories:")
    for idx, cat in enumerate(MEDIA_LIB.keys(), 1):
        print(f"{idx}) {cat}")
    print("0) Back")

def browse_category():
    list_categories()
    try:
        sel = int(input("> "))
        if sel == 0:
            return
        cats = list(MEDIA_LIB.keys())
        if 1 <= sel <= len(cats):
            cat = cats[sel-1]
            sources = MEDIA_LIB[cat]
            print(f"\nBrowse {cat}:")
            for j, item in enumerate(sources, 1):
                name, url, desc = item[:3]
                print(f"   {j}) {name} - {desc}\n      {url}")
            print("   0) Back")
            sub_sel = int(input("> "))
            if sub_sel == 0:
                return
            if 1 <= sub_sel <= len(sources):
                name, url, desc = sources[sub_sel-1][:3]
                print(f"\nOpening {name}...")
                webbrowser.open(url)
                log_access(cat, name, url)
                fav = input("Add to favorites? (y/n): ").strip().lower() == "y"
                if fav:
                    save_favorite(name, url)
    except Exception as e:
        print("Navigation error:", e)

def smart_search():
    query = input("\nEnter a keyword, title, or tag (or 0 to back): ").strip().lower()
    if query == "0":
        return
    matches = []
    for cat, items in MEDIA_LIB.items():
        for idx, item in enumerate(items, 1):
            name, url, desc = item[:3]
            if query in name.lower() or query in desc.lower() or query in cat.lower():
                matches.append((cat, idx, name, url, desc))
    if not matches:
        print("No results found.")
        return
    print(f"\nResults for '{query}':")
    for n, (cat, idx, name, url, desc) in enumerate(matches, 1):
        print(f"{n}) [{cat}] {name} - {desc}\n    {url}")
    sel = input("Open which? (number or 0 to back): ")
    if sel.isdigit() and 1 <= int(sel) <= len(matches):
        _, _, name, url, _ = matches[int(sel)-1]
        print(f"Opening {name}...")
        webbrowser.open(url)

def show_trending(top_n=10):
    print("\nTrending / Most Accessed:")
    if not os.path.exists(LOG_FILE):
        print("No usage log yet.")
        return
    from collections import Counter
    with open(LOG_FILE, "r") as f:
        lines = [l for l in f.readlines() if l.strip()]
    recents = [l.split("|")[2] for l in lines][-200:]
    counts = Counter(recents)
    most_common = counts.most_common(top_n)
    shown = set()
    for name, count in most_common:
        for cat, items in MEDIA_LIB.items():
            for idx, item in enumerate(items, 1):
                if item[0] == name and (cat, idx) not in shown:
                    print(f"{name} ({cat}) - Accesses: {count}")
                    shown.add((cat, idx))

def save_favorite(name, url):
    with open(FAVORITES_FILE, "a") as f:
        f.write(f"{name}|{url}\n")
    print("Added to favorites!")

def show_favorites():
    print("\nFavorites:")
    if not os.path.exists(FAVORITES_FILE):
        print("No favorites yet.")
        return
    with open(FAVORITES_FILE) as f:
        favs = [line.strip().split('|') for line in f.readlines()]
    for idx, (name, url) in enumerate(favs, 1):
        print(f"{idx}) {name}: {url}")
    print("0) Back")
    sel = input("> ")
    if sel.isdigit() and int(sel) in range(1, len(favs)+1):
        name, url = favs[int(sel)-1]
        webbrowser.open(url)

def add_note():
    print("\n-- Add Note --")
    url = input("Paste the resource URL (or 0 to back): ").strip()
    if url == "0":
        return
    note = input("Enter your note: ").strip()
    ts = datetime.datetime.now().isoformat()
    with open(NOTES_FILE, "a") as f:
        f.write(f"{ts}|{url}|{note}\n")
    print("Note saved!")

def show_notes():
    print("\nYour Notes:")
    if not os.path.exists(NOTES_FILE):
        print("No notes yet.")
        return
    with open(NOTES_FILE) as f:
        for line in f:
            parts = line.strip().split("|",2)
            print(f"[{parts[0]}]\n{parts[1]}\nNote: {parts[2]}\n")

def log_access(category, name, url, note=""):
    ts = datetime.datetime.now().isoformat()
    htext = f"{ts}|{category}|{name}|{url}|{MEDIA_COMPANION_FORMULA}|{note}"
    h = hashlib.sha256(htext.encode()).hexdigest()
    with open(LOG_FILE, "a") as f:
        f.write(f"{ts}|{category}|{name}|{url}|{note}|{h}\n")

def session_summary():
    if not os.path.isfile(LOG_FILE):
        print("No log entries.")
        return
    with open(LOG_FILE) as f:
        lines = f.readlines()
    print(f"\n-- Golden Fold Session Summary --")
    for line in lines[-20:]:
        print(line.strip())
    print(f"-- [Session End, {MEDIA_COMPANION_TIMESTAMP}] --\n")

# --- END OF CHUNK 3 ---
# Next: CHUNK 4 will add user profiles, ratings, export/import, AI suggestions, accessibility, and further expert features.
# Paste CHUNK 4 directly below this comment to continue.
# --- CHUNK 4: USER PROFILES, RATINGS, EXPORT/IMPORT, AI, ACCESSIBILITY ---

USER_PROFILES_FILE = "golden_fold_user_profiles.json"
ACTIVE_USER = None
USER_DATA = {}

def load_user_profiles():
    global USER_DATA
    if os.path.isfile(USER_PROFILES_FILE):
        with open(USER_PROFILES_FILE, "r", encoding="utf-8") as f:
            USER_DATA = json.load(f)
    else:
        USER_DATA = {}

def save_user_profiles():
    with open(USER_PROFILES_FILE, "w", encoding="utf-8") as f:
        json.dump(USER_DATA, f, indent=2)

def user_login():
    global ACTIVE_USER
    load_user_profiles()
    if not USER_DATA:
        print("\nNo user profiles found. Let's create one!")
        user_create()
        return
    print("\nChoose a user profile:")
    for idx, uname in enumerate(USER_DATA.keys(), 1):
        print(f"{idx}) {uname}")
    print("0) Create new profile")
    sel = input("> ").strip()
    if sel == "0":
        user_create()
        return
    users = list(USER_DATA.keys())
    if sel.isdigit() and 1 <= int(sel) <= len(users):
        uname = users[int(sel)-1]
        pin = input("Enter PIN (or leave blank if none): ").strip()
        if USER_DATA[uname].get("pin") and USER_DATA[uname]["pin"] != pin:
            print("Incorrect PIN.")
            return user_login()
        ACTIVE_USER = uname
        print(f"Welcome, {ACTIVE_USER}!")
    else:
        print("Invalid choice.")
        return user_login()

def user_create():
    global ACTIVE_USER
    uname = input("Choose a username: ").strip()
    if uname in USER_DATA:
        print("Username already exists.")
        return user_create()
    pin = input("Set a 4-digit PIN (optional, blank for none): ").strip()
    USER_DATA[uname] = {
        "pin": pin if pin else "",
        "favorites": [],
        "notes": [],
        "log": []
    }
    save_user_profiles()
    ACTIVE_USER = uname
    print(f"Profile created for {ACTIVE_USER}!")

def user_switch():
    print("\nSwitching user...")
    user_login()

def save_favorite(name, url):
    if ACTIVE_USER:
        USER_DATA[ACTIVE_USER]["favorites"].append({"name": name, "url": url})
        save_user_profiles()
        print("Added to favorites!")
    else:
        with open(FAVORITES_FILE, "a") as f:
            f.write(f"{name}|{url}\n")
        print("Added to favorites! (No user profile active)")

def show_favorites():
    print(f"\nFavorites ({ACTIVE_USER if ACTIVE_USER else 'Default'}):")
    if ACTIVE_USER:
        favs = USER_DATA[ACTIVE_USER].get("favorites", [])
        if not favs:
            print("No favorites yet.")
            return
        for idx, fav in enumerate(favs, 1):
            print(f"{idx}) {fav['name']}: {fav['url']}")
        print("0) Back")
        sel = input("> ")
        if sel.isdigit() and int(sel) in range(1, len(favs)+1):
            url = favs[int(sel)-1]['url']
            webbrowser.open(url)
    else:
        if not os.path.exists(FAVORITES_FILE):
            print("No favorites yet.")
            return
        with open(FAVORITES_FILE) as f:
            favs = [line.strip().split('|') for line in f.readlines()]
        for idx, (name, url) in enumerate(favs, 1):
            print(f"{idx}) {name}: {url}")
        print("0) Back")
        sel = input("> ")
        if sel.isdigit() and int(sel) in range(1, len(favs)+1):
            name, url = favs[int(sel)-1]
            webbrowser.open(url)

def add_note():
    print("\n-- Add Note --")
    url = input("Paste the resource URL (or 0 to back): ").strip()
    if url == "0": return
    note = input("Enter your note: ").strip()
    ts = datetime.datetime.now().isoformat()
    if ACTIVE_USER:
        USER_DATA[ACTIVE_USER]["notes"].append({"ts": ts, "url": url, "note": note})
        save_user_profiles()
        print("Note saved!")
    else:
        with open(NOTES_FILE, "a") as f:
            f.write(f"{ts}|{url}|{note}\n")
        print("Note saved! (No user profile active)")

def show_notes():
    print(f"\nYour Notes ({ACTIVE_USER if ACTIVE_USER else 'Default'}):")
    if ACTIVE_USER:
        notes = USER_DATA[ACTIVE_USER].get("notes", [])
        if not notes:
            print("No notes yet.")
            return
        for n in notes:
            print(f"[{n['ts']}]\n{n['url']}\nNote: {n['note']}\n")
    else:
        if not os.path.exists(NOTES_FILE):
            print("No notes yet.")
            return
        with open(NOTES_FILE) as f:
            for line in f:
                parts = line.strip().split("|",2)
                print(f"[{parts[0]}]\n{parts[1]}\nNote: {parts[2]}\n")

def log_access(category, name, url, note=""):
    ts = datetime.datetime.now().isoformat()
    htext = f"{ts}|{category}|{name}|{url}|{MEDIA_COMPANION_FORMULA}|{note}"
    h = hashlib.sha256(htext.encode()).hexdigest()
    if ACTIVE_USER:
        USER_DATA[ACTIVE_USER]["log"].append({
            "ts": ts, "category": category, "name": name, "url": url, "note": note, "hash": h
        })
        save_user_profiles()
    else:
        with open(LOG_FILE, "a") as f:
            f.write(f"{ts}|{category}|{name}|{url}|{note}|{h}\n")

def session_summary():
    if ACTIVE_USER:
        logs = USER_DATA[ACTIVE_USER].get("log", [])
        print(f"\n-- Session Summary for {ACTIVE_USER} --")
        for entry in logs[-20:]:
            print(f"{entry['ts']}|{entry['category']}|{entry['name']}|{entry['url']}|{entry['note']}|{entry['hash']}")
        print(f"-- [Session End, {MEDIA_COMPANION_TIMESTAMP}] --\n")
    else:
        if not os.path.isfile(LOG_FILE):
            print("No log entries.")
            return
        with open(LOG_FILE) as f:
            lines = f.readlines()
        print(f"\n-- Golden Fold Session Summary --")
        for line in lines[-20:]:
            print(line.strip())
        print(f"-- [Session End, {MEDIA_COMPANION_TIMESTAMP}] --\n")

def rate_resource(cat, idx):
    key = f"{cat}-{idx}"
    if ACTIVE_USER:
        user_scores = USER_DATA[ACTIVE_USER].get("scores", {})
    else:
        user_scores = load_user_scores()
    score = input("Rate 0-10 (or blank to skip): ").strip()
    if score.isdigit() and 0 <= int(score) <= 10:
        score = int(score)
        prev = user_scores.get(key, {"user": 0, "count": 0})
        new_count = prev["count"] + 1
        user_avg = (prev["user"] * prev["count"] + score) / new_count
        user_scores[key] = {"user": round(user_avg, 2), "count": new_count}
        print(f"Thank you! Current avg: {user_scores[key]['user']} ({new_count} votes)")
        if ACTIVE_USER:
            USER_DATA[ACTIVE_USER]["scores"] = user_scores
            save_user_profiles()
        else:
            save_user_scores(user_scores)
    else:
        print("Score not updated.")

def load_user_scores():
    if not os.path.isfile(USER_SCORES_FILE):
        return {}
    with open(USER_SCORES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_user_scores(scores):
    with open(USER_SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2)

def show_rankings(by="user", genre=None):
    if ACTIVE_USER:
        user_scores = USER_DATA[ACTIVE_USER].get("scores", {})
    else:
        user_scores = load_user_scores()
    ranked = []
    for cat, items in MEDIA_LIB.items():
        if genre and genre.lower() not in cat.lower():
            continue
        for idx, item in enumerate(items, 1):
            name, url, desc = item[:3]
            key = f"{cat}-{idx}"
            user = user_scores.get(key, {}).get("user", None)
            ranked.append((cat, idx, name, url, desc, user))
    ranked.sort(key=lambda x: (x[5] if x[5] is not None else 0), reverse=True)
    print("\n-- Top Ranked Resources --")
    for rank, (cat, idx, name, url, desc, user) in enumerate(ranked[:20], 1):
        print(f"{rank}. [{cat}] {name}: {desc} | User Avg: {user if user else '-'}\n    {url}")

def export_logs():
    files = [LOG_FILE, FAVORITES_FILE, NOTES_FILE, USER_SCORES_FILE, USER_PROFILES_FILE]
    zlist = [f for f in files if os.path.isfile(f)]
    if not zlist:
        print("No logs to export.")
        return
    zipname = f"GFMediaBundle_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    with zipfile.ZipFile(zipname, "w") as zipf:
        for f in zlist:
            zipf.write(f)
    print(f"Archived to {zipname} for backup/share! SHA256: {sha256_file(zipname)}")

def import_logs():
    print("Paste the path to your exported ZIP (or 0 to back):")
    path = input("> ").strip()
    if path == "0":
        return
    if not os.path.isfile(path):
        print("File not found.")
        return
    try:
        with zipfile.ZipFile(path, "r") as zipf:
            zipf.extractall()
        print("Import complete.")
    except Exception as e:
        print("Import failed:", e)

# Accessibility options
HIGH_CONTRAST = False
LARGE_FONT = False

def toggle_accessibility():
    global HIGH_CONTRAST, LARGE_FONT
    print("\nAccessibility Options:")
    print(f"1) Toggle High Contrast Mode (currently {'ON' if HIGH_CONTRAST else 'OFF'})")
    print(f"2) Toggle Large Font (currently {'ON' if LARGE_FONT else 'OFF'})")
    print("0) Back")
    sel = input("> ").strip()
    if sel == "1":
        HIGH_CONTRAST = not HIGH_CONTRAST
        print(f"High Contrast Mode {'enabled' if HIGH_CONTRAST else 'disabled'}.")
    elif sel == "2":
        LARGE_FONT = not LARGE_FONT
        print(f"Large Font {'enabled' if LARGE_FONT else 'disabled'}.")
    elif sel == "0":
        return
    else:
        print("Invalid choice.")

# AI-powered suggestions (rule-based for now)
def ai_suggestions():
    print("\nAI-Powered Suggestions (Beta)")
    genre_counts = {}
    if ACTIVE_USER:
        logs = USER_DATA[ACTIVE_USER].get("log", [])
        for entry in logs:
            genre_counts[entry["category"]] = genre_counts.get(entry["category"], 0) + 1
    elif os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) > 1:
                    cat = parts[1]
                    genre_counts[cat] = genre_counts.get(cat, 0) + 1
    if genre_counts:
        top_genre = max(genre_counts, key=genre_counts.get)
        print(f"Your most accessed category is: {top_genre}")
        # Suggest top 3 in that category not yet accessed
        accessed_names = set()
        if ACTIVE_USER:
            for entry in USER_DATA[ACTIVE_USER].get("log", []):
                accessed_names.add(entry["name"])
        else:
            with open(LOG_FILE, "r") as f:
                for line in f:
                    if "|" in line:
                        accessed_names.add(line.split("|")[2])
        suggestions = []
        for idx, item in enumerate(MEDIA_LIB.get(top_genre, []), 1):
            name, url, desc = item[:3]
            if name not in accessed_names:
                suggestions.append((name, url, desc))
            if len(suggestions) >= 3:
                break
        if suggestions:
            print("You might like:")
            for i, (name, url, desc) in enumerate(suggestions, 1):
                print(f"{i}) {name} - {desc}\n    {url}")
            sel = input("Open which? (number or 0 to back): ")
            if sel.isdigit() and 1 <= int(sel) <= len(suggestions):
                name, url, _ = suggestions[int(sel)-1]
                webbrowser.open(url)
        else:
            print("You've accessed everything in your top category! Try another genre.")
    else:
        print("No usage data yet. Explore and come back for suggestions!")

def main_menu():
    print(f"\nGolden Fold Quantum Media Companion {MEDIA_COMPANION_VERSION}")
    print(f"© 2025 Clayton Alexander McKinney\n{MEDIA_COMPANION_TIMESTAMP}")
    print(f"Formula: {MEDIA_COMPANION_FORMULA}")
    print(f"Formula established: {MEDIA_COMPANION_FORMULA_DATE}\n")
    print(f"Active User: {ACTIVE_USER if ACTIVE_USER else 'None'}")
    print("1) Explore by Category")
    print("2) Smart Search")
    print("3) Trending Now")
    print("4) Favorites")
    print("5) Add Note")
    print("6) Show Notes")
    print("7) Rate & Rankings")
    print("8) Session Summary")
    print("9) Export Logs/Notes")
    print("10) Import Logs/Notes")
    print("11) AI Suggestions")
    print("12) Accessibility Options")
    print("13) Switch User")
    print("0) Exit")
    return input("> ").strip()

def main():
    load_user_profiles()
    if not ACTIVE_USER:
        user_login()
    while True:
        choice = main_menu()
        if choice == "1":
            browse_category()
        elif choice == "2":
            smart_search()
        elif choice == "3":
            show_trending()
        elif choice == "4":
            show_favorites()
        elif choice == "5":
            add_note()
        elif choice == "6":
            show_notes()
        elif choice == "7":
            list_categories()
            cat_sel = input("Category number (or 0 to back): ")
            if cat_sel.isdigit() and int(cat_sel) in range(1, len(MEDIA_LIB)+1):
                cat = list(MEDIA_LIB.keys())[int(cat_sel)-1]
                sources = MEDIA_LIB[cat]
                for j, item in enumerate(sources, 1):
                    name, url, desc = item[:3]
                    print(f"   {j}) {name} - {desc}")
                res_sel = input("Resource number to rate (or 0 to back): ")
                if res_sel.isdigit() and int(res_sel) in range(1, len(sources)+1):
                    rate_resource(cat, int(res_sel))
            show_rankings()
        elif choice == "8":
            session_summary()
        elif choice == "9":
            export_logs()
        elif choice == "10":
            import_logs()
        elif choice == "11":
            ai_suggestions()
        elif choice == "12":
            toggle_accessibility()
        elif choice == "13":
            user_switch()
        elif choice == "0":
            print("Goodbye - your Golden Fold Infinite Library will keep growing and fractalizing!")
            break
        else:
            print("Invalid choice.")

# --- END OF CHUNK 4 ---
# Golden Fold Quantum Media Companion v12 is now complete and ready for expert use.
# Paste all chunks in order for the full system.
# --- CHUNK 5: CLOUD SYNC, MULTI-LANGUAGE UI, STARTUP/SHUTDOWN, PERFORMANCE ---

# Multi-language UI support (expand as needed)
LANGUAGES = {
    "en": {
        "welcome": "Welcome to Golden Fold Quantum Media Companion",
        "exit": "Goodbye - your Golden Fold Infinite Library will keep growing and fractalizing!",
        "favorites": "Favorites",
        "notes": "Notes",
        "search": "Search",
        "trending": "Trending",
        "profile": "User Profile",
        "settings": "Settings",
        "back": "Back",
        "invalid": "Invalid choice.",
    },
    "es": {
        "welcome": "Bienvenido a Golden Fold Quantum Media Companion",
        "exit": "¡Adiós! Tu Biblioteca Infinita Golden Fold seguirá creciendo y fractalizándose.",
        "favorites": "Favoritos",
        "notes": "Notas",
        "search": "Buscar",
        "trending": "Tendencias",
        "profile": "Perfil de usuario",
        "settings": "Configuraciones",
        "back": "Atrás",
        "invalid": "Opción inválida.",
    }
    # Add more languages as desired
}

LANGUAGE = "en"

def t(key):
    return LANGUAGES.get(LANGUAGE, LANGUAGES["en"]).get(key, key)

def language_menu():
    print("\nChoose language / Elige idioma:")
    for idx, lang in enumerate(LANGUAGES.keys(), 1):
        print(f"{idx}) {lang}")
    sel = input("> ").strip()
    langs = list(LANGUAGES.keys())
    if sel.isdigit() and 1 <= int(sel) <= len(langs):
        global LANGUAGE
        LANGUAGE = langs[int(sel)-1]
        print(f"Language set to {LANGUAGE}.")

# Cloud sync/export/import stubs
def cloud_sync_menu():
    print("\nCloud Sync & Backup Options:")
    print("1) Export library data for upload (manual or to cloud)")
    print("2) Import library data from file")
    print("3) [Future] Google Drive integration")
    print("4) [Future] Dropbox integration")
    print("0) Back")
    sel = input("> ").strip()
    if sel == "1":
        export_logs()
    elif sel == "2":
        import_logs()
    elif sel == "3":
        print("Google Drive sync coming soon! For now, use manual ZIP export/import.")
    elif sel == "4":
        print("Dropbox sync coming soon! For now, use manual ZIP export/import.")
    elif sel == "0":
        return
    else:
        print("Invalid choice.")

# Performance optimization for mobile (Pydroid3/Galaxy S9)
def optimize_for_mobile():
    # Already lightweight; future: add async I/O if needed
    pass

# Startup/shutdown routines
def startup():
    print(f"\n{t('welcome')} ({MEDIA_COMPANION_VERSION})")
    optimize_for_mobile()
    load_user_profiles()
    if not ACTIVE_USER:
        user_login()

def shutdown():
    print("\nShutting down Golden Fold Quantum Media Companion...")
    save_user_profiles()
    print(t("exit"))

# Main menu (final polish, now includes language & cloud sync)
def main_menu():
    print(f"\nGolden Fold Quantum Media Companion {MEDIA_COMPANION_VERSION}")
    print(f"© 2025 Clayton Alexander McKinney\n{MEDIA_COMPANION_TIMESTAMP}")
    print(f"Formula: {MEDIA_COMPANION_FORMULA}")
    print(f"Formula established: {MEDIA_COMPANION_FORMULA_DATE}\n")
    print(f"Active User: {ACTIVE_USER if ACTIVE_USER else 'None'}")
    print("1) Explore by Category")
    print("2) Smart Search")
    print("3) Trending Now")
    print("4) Favorites")
    print("5) Add Note")
    print("6) Show Notes")
    print("7) Rate & Rankings")
    print("8) Session Summary")
    print("9) Export Logs/Notes")
    print("10) Import Logs/Notes")
    print("11) AI Suggestions")
    print("12) Accessibility Options")
    print("13) Switch User")
    print("14) Cloud Sync & Backup")
    print("15) Language / Idioma")
    print("0) Exit")
    return input("> ").strip()

def main():
    startup()
    while True:
        choice = main_menu()
        if choice == "1":
            browse_category()
        elif choice == "2":
            smart_search()
        elif choice == "3":
            show_trending()
        elif choice == "4":
            show_favorites()
        elif choice == "5":
            add_note()
        elif choice == "6":
            show_notes()
        elif choice == "7":
            list_categories()
            cat_sel = input("Category number (or 0 to back): ")
            if cat_sel.isdigit() and int(cat_sel) in range(1, len(MEDIA_LIB)+1):
                cat = list(MEDIA_LIB.keys())[int(cat_sel)-1]
                sources = MEDIA_LIB[cat]
                for j, item in enumerate(sources, 1):
                    name, url, desc = item[:3]
                    print(f"   {j}) {name} - {desc}")
                res_sel = input("Resource number to rate (or 0 to back): ")
                if res_sel.isdigit() and int(res_sel) in range(1, len(sources)+1):
                    rate_resource(cat, int(res_sel))
            show_rankings()
        elif choice == "8":
            session_summary()
        elif choice == "9":
            export_logs()
        elif choice == "10":
            import_logs()
        elif choice == "11":
            ai_suggestions()
        elif choice == "12":
            toggle_accessibility()
        elif choice == "13":
            user_switch()
        elif choice == "14":
            cloud_sync_menu()
        elif choice == "15":
            language_menu()
        elif choice == "0":
            shutdown()
            break
        else:
            print(t("invalid"))

# --- END OF CHUNK 5 ---
# Golden Fold Quantum Media Companion v12 is now a seamless, expert-level, future-proof system.
# Paste all chunks in order for the full experience.
# --- CHUNK 6: MOBILE OPTIMIZATION FOR PYDROID3 & GALAXY S9 ---

def mobile_performance_tips():
    print("\nPerformance tips for Galaxy S9/Pydroid3:")
    print("- Regularly use Device Care/Device Maintenance to clear memory and optimize.")
    print("- In Developer Options, set all animation scales (window, transition, animator) to 0.5x or off for faster UI.")
    print("- For games or heavy web pages, close other apps first.")
    print("- Use the 'Optimize Now' button in Device Care for a quick speed boost.")
    print("- If you experience lag, reboot your phone or clear cache partition.")
    print("- Avoid running too many background apps or widgets.")
    print("- For best results, keep your Pydroid3 and Python libraries up to date.")

def optimize_for_mobile():
    # This function is called at startup for reminders and any future tweaks
    mobile_performance_tips()

def startup():
    print(f"\n{t('welcome')} ({MEDIA_COMPANION_VERSION})")
    optimize_for_mobile()
    load_user_profiles()
    if not ACTIVE_USER:
        user_login()

def shutdown():
    print("\nShutting down Golden Fold Quantum Media Companion...")
    save_user_profiles()
    print(t("exit"))

def main():
    startup()
    while True:
        choice = main_menu()
        if choice == "1":
            browse_category()
        elif choice == "2":
            smart_search()
        elif choice == "3":
            show_trending()
        elif choice == "4":
            show_favorites()
        elif choice == "5":
            add_note()
        elif choice == "6":
            show_notes()
        elif choice == "7":
            list_categories()
            cat_sel = input("Category number (or 0 to back): ")
            if cat_sel.isdigit() and int(cat_sel) in range(1, len(MEDIA_LIB)+1):
                cat = list(MEDIA_LIB.keys())[int(cat_sel)-1]
                sources = MEDIA_LIB[cat]
                for j, item in enumerate(sources, 1):
                    name, url, desc = item[:3]
                    print(f"   {j}) {name} - {desc}")
                res_sel = input("Resource number to rate (or 0 to back): ")
                if res_sel.isdigit() and int(res_sel) in range(1, len(sources)+1):
                    rate_resource(cat, int(res_sel))
            show_rankings()
        elif choice == "8":
            session_summary()
        elif choice == "9":
            export_logs()
        elif choice == "10":
            import_logs()
        elif choice == "11":
            ai_suggestions()
        elif choice == "12":
            toggle_accessibility()
        elif choice == "13":
            user_switch()
        elif choice == "14":
            cloud_sync_menu()
        elif choice == "15":
            language_menu()
        elif choice == "0":
            shutdown()
            break
        else:
            print(t("invalid"))

# --- END OF CHUNK 6 ---
# This is the final chunk for a seamless, mobile-optimized, expert-level library system on Pydroid3/Galaxy S9.
# Paste all chunks in order for the complete system.
if __name__ == "__main__":
    main()
