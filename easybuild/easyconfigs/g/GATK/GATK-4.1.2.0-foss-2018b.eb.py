##
# EasyBuild Easyconfig
#
# Copyright:: Copyright 2012-2013 Cyprus Institute /
# CaSToRC, University of Luxembourg / LCSB
# Authors::   George Tsouloupas <g.tsouloupas@cyi.ac.cy>,
#             Fotis Georgatos <fotis.georgatos@uni.lu>,
#             Kenneth Hoste (UGent)
# License::   MIT/GPL
# $Id$
#
# This work implements a part of the HPCBIOS project and is a component
# of the policy: http://hpcbios.readthedocs.org/en/latest/HPCBIOS_2012-94.html
# Modified by: Adam Huffman, Jonas Demeulemeester
# The Francis Crick Institute
# Modified for version 4.0.5.1 by: Ruben van Dijk, University of Groningen
# Modifed for version 4.1.2.0 by: T. Medina, UMC Groningen
##

easyblock = 'Tarball'

name = 'GATK'
version = '4.1.2.0'
# versionsuffix = '-Python-%(pyver)s'

homepage = 'http://www.broadinstitute.org/gatk/'
description = """The Genome Analysis Toolkit or GATK is a software package
developed at the Broad Institute to analyse next-generation resequencing
data. The toolkit offers a wide variety of tools, with a primary focus on
variant discovery and genotyping as well as strong emphasis on data quality
assurance. Its robust architecture, powerful processing engine and
high-performance computing features make it capable of taking on projects
of any size."""

toolchain = {'name': 'foss', 'version': '2018b'}
source_urls = ['https://github.com/broadinstitute/gatk/releases/download/%(version)s/']
sources = ['gatk-%(version)s.zip']
checksums = ['ffc5f9b3d4b35772ee5dac3060b59dc657f30e830745160671d84d732c30dc65']

dependencies = [
        ('Java', '1.8', '', True),
        # ('Python', '3.6.3')
        ]

modextrapaths = {'PATH': ''}

sanity_check_paths = {
        'files': ['gatk'],
        'dirs': []
        }

sanity_check_commands = ["gatk --help"]

moduleclass = 'bio'
