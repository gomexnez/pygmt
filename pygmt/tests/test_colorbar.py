"""
Tests colorbar
"""
import pytest

from .. import Figure


@pytest.mark.mpl_image_compare
def test_colorbar_using_paper_coordinates():
    """
    Create colorbar positioned at 0cm,0cm with length 1cm and width 0.5cm.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_using_paper_coordinates_horizontal():
    """
    Create colorbar positioned at 0cm,0cm with length 2cm oriented horizontally
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", position="x0c/0c+w2c+h")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_positioned_using_map_coordinates():
    """
    Create colorbar positioned at longitude,latitude 3,6 with length 2cm.
    """
    fig = Figure()
    fig.basemap(region=[2, 4, 6, 8], projection="t0/2c", frame=True)
    fig.colorbar(cmap="rainbow", position="g3/6+w2c")
    return fig


@pytest.mark.xfail(
    reason="Baseline image not updated to use earth relief grid in GMT 6.1.0",
)
@pytest.mark.mpl_image_compare
def test_colorbar_positioned_using_justification_code():
    """
    Create colorbar at Top Center inside the map frame with length 2cm.
    """
    fig = Figure()
    fig.basemap(region=[2, 4, 6, 8], projection="t0/2c", frame=True)
    fig.colorbar(cmap="rainbow", position="jTC+w2c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_positioned_using_normalized_coords():
    """
    Create colorbar at normalized coordinates 0.75,0.25 with length 2cm.
    """
    fig = Figure()
    fig.basemap(region=[2, 4, 6, 8], projection="t0/2c", frame=True)
    fig.colorbar(cmap="rainbow", position="n0.75/0.25+w2c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_box():
    """
    Create colorbar with box around it.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", box=True, position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_box_with_pen():
    """
    Create colorbar with box that has a different colored pen.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", box="+porange", position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_box_with_fill():
    """
    Create colorbar with box that has a different colored fill.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", box="+gorange", position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_box_with_clearance():
    """
    Create colorbar with box that has an x-clearance of 0.8cm and y-clearance
    of 0.4cm.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", box="+c0.8c/0.4c+porange", position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_box_with_secondary_border():
    """
    Create colorbar with box that has a secondary, inner border in addition to
    the main primary, outer border.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", box="+porange+imagenta", position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_box_with_rounded_corners():
    """
    Create colorbar with box that has rounded corners.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", box="+porange+r", position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_box_with_offset_background():
    """
    Create colorbar with box and an offset background shaded region.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", box="+s5p/-5p", position="x0c/0c+w1c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_truncated_to_zlow_zhigh():
    """
    Create colorbar truncated to z-low and z-high.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", truncate=[0.15, 0.85], position="x0c/0c+w2c/0.5c")
    return fig


@pytest.mark.mpl_image_compare
def test_colorbar_scaled_z_values():
    """
    Create colorbar with z-values scaled to 0.1x of the original CPT.
    """
    fig = Figure()
    fig.colorbar(cmap="rainbow", scale=0.1, position="x0c/0c+w2c/0.5c")
    return fig
