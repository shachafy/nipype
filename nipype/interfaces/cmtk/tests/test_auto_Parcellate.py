# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..parcellation import Parcellate


def test_Parcellate_inputs():
    input_map = dict(
        dilation=dict(usedefault=True, ),
        freesurfer_dir=dict(),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        out_roi_file=dict(genfile=True, ),
        parcellation_name=dict(usedefault=True, ),
        subject_id=dict(mandatory=True, ),
        subjects_dir=dict(),
    )
    inputs = Parcellate.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Parcellate_outputs():
    output_map = dict(
        aseg_file=dict(),
        cc_unknown_file=dict(),
        dilated_roi_file_in_structural_space=dict(),
        ribbon_file=dict(),
        roi_file=dict(),
        roi_file_in_structural_space=dict(),
        roiv_file=dict(),
        white_matter_mask_file=dict(),
    )
    outputs = Parcellate.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
