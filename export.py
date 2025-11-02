from django.core.management import call_command
from django.core import serializers
from django.conf import settings
from django.db import connection
import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

EXPORT_MODELS = [
    'activity.Activity',
    'activity.ActivityImage',
    'collection.Collection',
    'collection.CollectionImage',
    'index.Banner',
    'index.Quotes',
    'index.News',
    'index.NewsImage',
    'index.Notice',
    'index.NoticeImage',
    'kenshi.Kenshi',
    'kenshi.KenshiImage',
    'others.About',
    'others.Contact',
    'others.Terms',
    'others.Part',
    'others.Section',
    'others.Privacy',
    'others.Faq',
    'member.CustomUser',
]


OUTPUT_DIR = os.path.join(BASE_DIR, 'export_data')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def export_to_json():
    for model_path in EXPORT_MODELS:
        app_label, model_name = model_path.split('.')
        try:
            Model = django.apps.apps.get_model(app_label, model_name)
        except LookupError:
            print(f"[!] Model not found: {model_path}")
            continue

        queryset = Model.objects.all()
        count = queryset.count()
        if count == 0:
            print(f"[i] {model_path} No information available, skipped.")
            continue

        filename = f"{app_label}_{model_name.lower()}.json"
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            serializers.serialize('json', queryset, stream=f, indent=2, ensure_ascii=False)

        print(f"[Success] {model_path} → {filename} ({count} record{'s' if count != 1 else ''})")


def import_from_json():
    import_path = OUTPUT_DIR
    if not os.path.exists(import_path):
        print(f"[Error] Directory not found: {import_path}")
        return

    json_files = [f for f in os.listdir(import_path) if f.endswith('.json')]
    if not json_files:
        print(f"[i] No JSON files found in {import_path}")
        return

    print(f"[i] Found {len(json_files)} file(s) to import:")
    for f in json_files:
        print(f"   • {f}")

    if not confirm("Proceed with import?", default=False):
        print("Data import cancelled.")
        return

    total = 0
    for filename in json_files:
        filepath = os.path.join(import_path, filename)
        try:
            print(f"Importing {filename}...", end=" ")
            call_command('loaddata', filepath, verbosity=0)
            with open(filepath, 'r', encoding='utf-8') as f:
                data = f.read().count('"pk":')
            print(f"Success ({data} record{'s' if data != 1 else ''})")
            total += data
        except Exception as e:
            print(f"Failed: {e}")

    print(f"\n[Summary] Successfully imported {total} record{'s' if total != 1 else ''}.")


def confirm(prompt, default=False):
    while True:
        choice = input(f"{prompt} [{'Y/n' if default else 'y/N'}]: ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        elif choice == '':
            return default
        else:
            print("y/n")


def main_menu():
    print("\n" + "="*50)
    print("    Django Data Export Tool")
    print("="*50)

    # Option 1: Export data
    if confirm("Do you want to export data?", default=True):
        export_to_json()
    else:
        print("Data export cancelled.")

    # Option 2: Format database
    if confirm("Do you want to format the database (delete all data)?", default=False):
        if confirm("WARNING: This will delete ALL data! Are you sure you want to continue?", default=False):
            print("Formatting database...")
            call_command('flush', '--no-input')
            print("[Success] Database has been formatted (all data cleared).")
        else:
            print("Database formatting cancelled.")
    else:
        print("Skipping database formatting.")

    # Option 3: Import data
    if confirm("Do you want to import data from JSON files?", default=False):
        import_from_json()
    else:
        print("Data import skipped.")


if __name__ == '__main__':
    main_menu()
