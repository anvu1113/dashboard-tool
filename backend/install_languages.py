import argostranslate.package
import argostranslate.translate

def install_languages():
    print("Updating package index...")
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    
    # Install en <-> vi
    # Argos Translate uses pivot through English usually, so we need:
    # Any specific pairs.
    # Let's install en->vi and vi->en
    
    pairs_to_install = [
        ('en', 'vi'),
        ('vi', 'en')
    ]
    
    for from_code, to_code in pairs_to_install:
        print(f"Looking for {from_code} -> {to_code}...")
        package_to_install = next(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
            ), None
        )
        
        if package_to_install:
            print(f"Installing {from_code} -> {to_code}...")
            argostranslate.package.install_from_path(package_to_install.download())
        else:
            print(f"Package {from_code} -> {to_code} not found.")

if __name__ == "__main__":
    install_languages()
