import os
import sys

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
required = ['SKILL.md', 'package.json', 'CHANGELOG.md', 'LICENSE', 'brand.json', '.tidyfactor', 'README.md', 'README.ar.md']

missing = [f for f in required if not os.path.exists(os.path.join(base, f))]
if missing:
    print(f'[FAIL] Missing files: {missing}')
    sys.exit(1)
print('[PASS] tidyfactor-doc structural validation passed 100%!')

