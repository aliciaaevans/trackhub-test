import glob, os, re
import trackhub

# First we initialize the components of a track hub

hub, genomes_file, genome, trackdb = trackhub.default_hub(
    hub_name="Variant Calling Demo",
    short_label='vcf_demo',
    long_label='variant_calling_demo',
    genome="hg38",
    email="alicia.evans@nih.gov")


for path in glob.glob(os.path.join("trackhub-test/variant_calling_demo/hg38", "*.bam")):
    file = os.path.basename(path)
    label = re.sub('[^0-9a-zA-Z]+', '', file)
    bam = trackhub.Track(
        tracktype="bam",
        name=label,
        description=label,
        pairEndsByName=".",
        pairSearchRange="10000",
        chromosomes="chr6,chr20",
        maxWindowToDraw="200000",
        visibility="pack",
        bigDataUrl=file,
    )
    # Each track is added to the trackdb
    trackdb.add_tracks(bam)

for path in glob.glob(os.path.join("trackhub-test/variant_calling_demo/hg38", "*.vcf.gz")):
    file = os.path.basename(path)
    label = re.sub('[^0-9a-zA-Z]+', '', file)
    vcf = trackhub.Track(
        tracktype="vcfTabix",
        name=label,
        chromosomes="chr6,chr20",
        visibility="pack",
        url=file,
    )
    # Each track is added to the trackdb
    trackdb.add_tracks(vcf)



# In this example we "upload" the hub locally. Files are created in the
# "example_hub" directory, along with symlinks to the tracks' data files.
# This directory can then be pushed to GitHub or rsynced to a server.

trackhub.upload.upload_hub(hub=hub, host='localhost', remote_dir='trackhub-test/variant_calling_demo')
