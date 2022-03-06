import astropy.units as u
import sunpy.map
from sunpy.data.sample import AIA_193_IMAGE


def low_res_aia_193(resolution=[512, 512] * u.pix):
    return sunpy.map.Map(AIA_193_IMAGE).resample(resolution)
