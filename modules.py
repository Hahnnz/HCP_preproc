from nipype import Workflow, Node
from nipype.interfaces import utility as niu, fsl
from niworkflows.interfaces import NormalizeMotionParams
from niworkflows.interfaces.itk import MCFLIRT2ITK

def head_motion_correction(name='motion_correction'):
    workflow = Workflow(name)
    
    input_node = Node(
        niu.IdentityInterface(fields=['bold_file', 'raw_ref_image']), 
        name='input')
    output_node = Node(
        niu.IdentityInterface(fields=['xforms', 'movpar_file']),
        name='outputnode')
    
    mcflirt = Node(fsl.MCFLIRT(save_mats=True, save_plots=True), name='mcflirt')

    fsl2itk = Node(MCFLIRT2ITK(), name='fsl2itk')

    normalize_motion = Node(NormalizeMotionParams(format='FSL'), name="normalize_motion")

    workflow.connect([
        (input_node, mcflirt, [('raw_ref_image', 'ref_file'), ('bold_file', 'in_file')]),
        (input_node, fsl2itk, [('raw_ref_image', 'in_source'), ('raw_ref_image', 'in_reference')]),
        (mcflirt, fsl2itk, [('mat_file', 'in_files')]),
        (mcflirt, normalize_motion, [('par_file', 'in_file')]),
        (fsl2itk, output_node, [('out_file', 'xforms')]),
        (normalize_motion, output_node, [('out_file', 'movpar_file')]),
    ])
    
    return workflow