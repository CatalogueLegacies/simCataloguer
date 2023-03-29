from simCataloguer import Writer

outputdir = input("Write output folder name here: ")
writer = Writer()
writer(
    'MDG.txt',
    'simMDG',
    'outputs/hairout',
    f'outputs/{outputdir}'
    pixray_num_cuts=8,
    pixray_quality="draft"
)
