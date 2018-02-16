
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
    
import unittest
import numpy as np
import sys

from muesr.core.sample import Sample
from muesr.core.sampleErrors import *
from muesr.i_o.cif.cif import load_cif, read_cif

MnSi_cif=StringIO("""#------------------------------------------------------------------------------
#$Date: 2013-05-05 14:21:46 +0000 (Sun, 05 May 2013) $
#$Revision: 85285 $
#$URL: file:///home/coder/svn-repositories/cod/cif/9/01/39/9013972.cif $
#------------------------------------------------------------------------------
#
# This file is available in the Crystallography Open Database (COD),
# http://www.crystallography.net/. The original data for this entry
# were provided the American Mineralogist Crystal Structure Database,
# http://rruff.geo.arizona.edu/AMS/amcsd.php
#
# The file may be used within the scientific community so long as
# proper attribution is given to the journal article from which the
# data were obtained.
#
data_9013972
loop_
_publ_author_name
'Jorgensen, J. E.'
'Rasmussen, S. E.'
_publ_section_title
;
 Refinement of the structure of MnSi by powder diffraction
;
_journal_name_full               'Powder Diffraction'
_journal_page_first              194
_journal_page_last               195
_journal_volume                  6
_journal_year                    1991
_chemical_formula_structural     MnSi
_chemical_formula_sum            'Mn Si'
_chemical_name_mineral           Brownleeite
_space_group_IT_number           198
_symmetry_space_group_name_Hall  'P 2ac 2ab 3'
_symmetry_space_group_name_H-M   'P 21 3'
_cell_angle_alpha                90
_cell_angle_beta                 90
_cell_angle_gamma                90
_cell_length_a                   4.55643
_cell_length_b                   4.55643
_cell_length_c                   4.55643
_cell_volume                     94.596
_exptl_crystal_density_diffrn    5.830
_cod_database_code               9013972
loop_
_symmetry_equiv_pos_as_xyz
x,y,z
1/2-z,-x,1/2+y
-z,1/2+x,1/2-y
1/2+z,1/2-x,-y
z,x,y
1/2+y,1/2-z,-x
1/2-y,-z,1/2+x
-y,1/2+z,1/2-x
y,z,x
-x,1/2+y,1/2-z
1/2+x,1/2-y,-z
1/2-x,-y,1/2+z
loop_
_atom_site_label
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_U_iso_or_equiv
Mn 0.1380 0.1380 0.1380 0.00800
Si 0.84620 0.84620 0.84620 0.01600
""")


class TestCifIO(unittest.TestCase):
    def setUp(self):
        pass
    
    @unittest.skipIf(sys.version_info[0] >= 3, 'Python3 specific test')
    def test_open_invalid_file(self):
        s = Sample()
        with self.assertRaises(FileNotFoundError):
            load_cif(s,'ciao')
            
    @unittest.skipIf(sys.version_info[0] < 3, 'Python2 specific test')
    def test_open_invalid_file(self):
        s = Sample()
        with self.assertRaises(OSError):
            load_cif(s,'ciao')
    
        # check for python2
        with self.assertRaises(OSError):
            load_cif(s,u'ciao')
    
    def test_open_file(self):
        s = Sample()
        MnSi_cif.seek(0)  
        read_cif(MnSi_cif, 0)

        
if __name__ == '__main__':
    unittest.main()
