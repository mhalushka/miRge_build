import os
import sys
from scipy.spatial import cKDTree
import time
import cPickle
from Bio import SeqIO

def main(arg = sys.argv):
	if len(arg) != 4:
		print >> sys.stderr, 'build_bowtie_lib.py species PathOfBowtie-build PathOfIndex'
		sys.exit(1)
	else:
		species = arg[1]
		bowtie_build_path = os.path.join(arg[2], 'bowtie-build')
		#print bowtie_build_path
		PathOfIndex = arg[3]
		totalList = ['genome', 'hairpin_miRBase', 'hairpin_miRGeneDB', 'mirna_SNP_lib_miRBase', 'mirna_SNP_lib_miRGeneDB', 'mrna', 'ncrna_others', 'rrna', 'snorna', 'trna', 'spike-in']
		time1 = time.time()
		for type in totalList:
			if type != 'spike-in':
				if os.path.isfile(os.path.join(PathOfIndex, species+'_'+type+'.fa')):
					if 'lib' not in type:
						os.system('%s %s %s'%(bowtie_build_path, os.path.join(PathOfIndex, species+'_'+type+'.fa'), os.path.join(PathOfIndex, species+'_'+type)))
						print 'bowtie index file of %s is generated.'%(species+'_'+type)
					else:
						if 'miRBase' in type:
							os.system('%s %s %s'%(bowtie_build_path, os.path.join(PathOfIndex, species+'_'+type+'.fa'), os.path.join(PathOfIndex, species+'_mirna_miRBase')))
							print 'bowtie index file of %s is generated.'%(species+'_mirna_miRBase')
						else:
							os.system('%s %s %s'%(bowtie_build_path, os.path.join(PathOfIndex, species+'_'+type+'.fa'), os.path.join(PathOfIndex, species+'_mirna_miRGeneDB')))
							print 'bowtie index file of %s is generated.'%(species+'_mirna_miRGeneDB')
				else:
					print >> sys.stderr, 'The file "%s" does not exist. Please check it'%(os.path.join(PathOfIndex, species+'_'+type+'.fa'))
					sys.exit(1)
			else:
				if os.path.isfile(os.path.join(PathOfIndex, species+'_'+type+'.fa')):
					os.system('%s %s %s'%(bowtie_build_path, os.path.join(PathOfIndex, species+'_'+type+'.fa'), os.path.join(PathOfIndex, species+'_'+type)))
					print 'bowtie index file of %s is generated.'%(species+'_'+type)
				else:
					pass
		time2 = time.time()
		print "Building the bowtie index is done and it takes: %.1fs"%(time2-time1)

if __name__ == '__main__':
	main()