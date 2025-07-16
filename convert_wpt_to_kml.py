import xml.etree.ElementTree as ET

def convert_wpt_to_kml(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Creazione della struttura KML
    kml = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2")
    document = ET.SubElement(kml, "Document")
    
    for line in lines:
        parts = line.strip().split('\t')  # I dati sono separati da tabulazioni
        if len(parts) < 12:
            continue  # Salta righe non valide
        
        try:
            lat = float(parts[8])
            lon = float(parts[9])
            alt = float(parts[10])
        except ValueError:
            continue  # Salta righe con dati non validi
        
        placemark = ET.SubElement(document, "Placemark")
        ET.SubElement(placemark, "name").text = f"Waypoint {parts[0]}"
        ET.SubElement(placemark, "Point")
        coordinates = ET.SubElement(placemark.find("Point"), "coordinates")
        coordinates.text = f"{lon},{lat},{alt}"
    
    # Scrittura su file KML
    tree = ET.ElementTree(kml)
    with open(output_file, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

# Esempio di utilizzo
convert_wpt_to_kml("missione_ravenna.wpt", "mission.kml")
print("Conversione completata! Apri mission.kml in Google Earth.")
