from pathlib import Path
import os


# --- Common Path Vars ---
cwd = Path.cwd()

tech = Path(os.path.join(cwd, '00-TECH'))
tech_sum = sum(1 for item in tech.iterdir() if item.is_dir())

ecs = Path(os.path.join(cwd, '10-ESSENTIAL_CONSUMER_SERVICE'))
ecs_sum = sum(1 for item in ecs.iterdir() if item.is_dir())

core = Path(os.path.join(cwd, '20-CONSUMER_CORE'))
core_sum = sum(1 for item in core.iterdir() if item.is_dir())

brand = Path(os.path.join(cwd, '30-CONSUMER_BRAND'))
brand_sum = sum(1 for item in brand.iterdir() if item.is_dir())

ind = Path(os.path.join(cwd, '40-INDUSTRY_CORE'))
ind_sum = sum(1 for item in ind.iterdir() if item.is_dir())

med = Path(os.path.join(cwd, '50-MEDICAL'))
med_sum = sum(1 for item in med.iterdir() if item.is_dir())

mix = Path(os.path.join(cwd, '60-MIX'))
mix_sum = sum(1 for item in mix.iterdir() if item.is_dir())

reit = Path(os.path.join(cwd, '80-REIT'))
reit_sum = sum(1 for item in reit.iterdir() if item.is_dir())

# --- Stock Counts ---
print(f'\nNumber of Stocks in Group 0 TECH: {tech_sum}')
print(f'Number of Stocks in Group 1 ESSENTIAL_CONSUMER_SERVICE: {ecs_sum}')
print(f'Number of Stocks in Group 2 CONSUMER_CORE: {core_sum}')
print(f'Number of Stocks in Group 3 CONSUMER_BRAND: {brand_sum}')
print(f'Number of Stocks in Group 4 INDUSTRY_CORE: {ind_sum}')
print(f'Number of Stocks in Group 5 MEDICAL: {med_sum}')
print(f'Number of Stocks in Group 6 MIX: {mix_sum}')
print(f'Number of Stocks in Group 8 REIT: {reit}')
print(f'Total Stocks Covered: {tech_sum + ecs_sum + core_sum + brand_sum + ind_sum + med_sum + mix_sum + reit_sum}')