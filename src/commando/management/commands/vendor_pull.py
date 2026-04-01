from typing import Any
from django.core.management.base import BaseCommand
from helpers.downloader import download_to_local
from django.conf import settings


class Command(BaseCommand):
    def __init__(self):
        self.VENDORS_STATICFILES = getattr(settings, 'VENDORS_STATICFILES')
        self.STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')
        
    def handle(self, *args: Any, **options: Any):
        print(f'Downloading vendors files...\n')
        
        complete_urls = []
        
        for name, url in self.VENDORS_STATICFILES.items():
            print(f"Downloading {name} in {self.STATICFILES_VENDOR_DIR} ...")
            
            out_path = self.STATICFILES_VENDOR_DIR / name
            # print(name, url, out_path)
            success = download_to_local(url, out_path, True)
            
            if success:
                complete_urls.append(name)
            else:
                print(f"Ocorreu um erro ao efetuar o download de {name}")
            
            print("\n")
        
        for name in complete_urls:
            print(f"{name} succesfuly downloaded!")
            
            
