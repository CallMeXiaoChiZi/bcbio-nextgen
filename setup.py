#!/usr/bin/env python
"""Setup file and install script for NextGen sequencing analysis scripts.
"""
from setuptools import setup, find_packages

setup(name = "bcbio-nextgen",
      version = "0.1",
      author = "Brad Chapman",
      author_email = "chapmanb@50mail.com",
      description = "Automated, distributed next-gen sequencing pipeline; includes Galaxy interaction",
      license = "MIT",
      url = "http://bcbio.wordpress.com",
      namespace_packages = ["bcbio"],
      packages = find_packages(),
      scripts = ['scripts/analyze_finished_sqn.py',
                 'scripts/analyze_quality_recal.py',
                 'scripts/automated_initial_analysis.py',
                 'scripts/distributed_nextgen_pipeline.py',
                 'scripts/bam_to_wiggle.py',
                 'scripts/barcode_sort_trim.py',
                 'scripts/illumina_finished_msg.py',
                 'scripts/nextgen_analysis_server.py',
                 'scripts/solexa_qseq_to_fastq.py',
                 'scripts/store_finished_sqn.py',
                 'scripts/upload_to_galaxy.py',
                 'scripts/variant_effects.py',
                 ],
      package_data = {
          'config' : ['*.yaml'],
          },
      install_requires = [
          "biopython >= 1.56",
          "Mako >= 0.3.6",
          "PyYAML >= 3.09",
          "amqplib >= 0.6.1",
          "Logbook >= 0.3",
          "pysam >= 0.4.1",
          "fabric >= 1.0.1",
          "celery >= 2.2.7",
          #"rpy2 >= 2.0.7"
      ])
