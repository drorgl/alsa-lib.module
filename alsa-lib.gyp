{
	'variables':{
		'library' : 'shared_library',
		#'library' : 'static_library',
		#'alsa_lib_type' : 'full',
		'alsa_lib_type' : 'salsa',
	},
	'target_defaults': {
		'configurations': {
			'Debug' : {},
			'Release' : {},
		},
		
		'conditions':[
			['OS=="linux" and target_arch=="ia32"',{
				'cflags':[
					'-m32',
				],
				'ldflags':[
					'-m32',
					'-L/usr/lib32',
					'-L/usr/lib32/debug',
				],
			}],
			['OS=="linux" and target_arch=="x64"',{
				'cflags':[
					'-m64',
					
				],
				'ldflags':[
					'-m64',
				],
			}],	
			['target_arch=="x64" and library == "static_library"',{
				'cflags':[
					'-fvisibility=hidden',
				],
			}],
			['OS in "linux android"',{
				'defines':[
					'PIC', #for dynamic libraries only
				],
				'cflags':[
					'-fPIC',
				],
			}],
		],
		
	  },
		
	  
		'targets':[
			{
				'target_name':'clear_before_alsa',
				'type':'none',
				'hard_dependency':1,
				'actions':[
					{
						'action_name': 'remove_include_folder',
						'inputs' : [
							#'includes',
						],
						'outputs':[
							'includes',
						],
						'action':[
							'rm','-rf','<(_outputs)'
						],
					}
				],
			},
		
		
			{
				'target_name': 'alsa-lib',
				
				
				'hard_dependency':1,
				
				'conditions':[
					['OS == "win"',{
						'type':'none',
					},{
						'type':'<(library)',
						'dependencies':[
							'clear_before_alsa',
						],
					}],
				
					['alsa_lib_type == "full"',{
						'defines':[
							#'ALSA_CONFIG_DIR="/system/usr/share/alsa"',
							#'ALSA_DEVICE_DIRECTORY="/dev/snd/"'
							#'_POSIX_SOURCE',
							
							
						],
						'include_dirs':[
							'includes',
							#'include/alsa',
							'alsa-lib_src/include',
							'alsa-lib_config',
							'alsa-lib_config/include',
						],
						'direct_dependent_settings': {
							'defines':[
								#'_POSIX_SOURCE',
							],
							'include_dirs': [
								'includes',
								'alsa-lib_src/include',
								'alsa-lib_src/include/alsa',
								
							],
						},
						
						'copies':[
							{
								'destination':'includes',
								'files':[
									'alsa-lib_src/include/local.h',
								],
							},
							{
								'destination':'includes/alsa',
								'files':[
									'alsa-lib_config/include/asoundlib.h',
									'alsa-lib_config/version.h',
									'alsa-lib_src/include/asoundef.h',
									'alsa-lib_src/include/global.h',
									'alsa-lib_src/include/input.h',
									'alsa-lib_src/include/output.h',
									'alsa-lib_src/include/error.h',
									'alsa-lib_src/include/conf.h',
									'alsa-lib_src/include/pcm.h',
									'alsa-lib_src/include/rawmidi.h',
									'alsa-lib_src/include/timer.h',
									'alsa-lib_src/include/hwdep.h',
									'alsa-lib_src/include/control.h',
									'alsa-lib_src/include/mixer.h',
									'alsa-lib_src/include/seq_event.h',
									'alsa-lib_src/include/seq.h',
									'alsa-lib_src/include/seqmid.h',
									'alsa-lib_src/include/seq_midi_event.h',
								],
							},
							
						],
						
						'conditions':[
							['OS == "linux"',{
								'defines':[
									'ALSA_CONFIG_DIR="/usr/share/alsa"',
									'_GNU_SOURCE',
								],
								'link_settings':{
									'libraries':[
										'-ldl',
									],
								},
							}],
							['OS == "android"',{
								'defines':[
									'ALSA_CONFIG_DIR="/system/usr/share/alsa"',
									'_POSIX_SOURCE',
								],
								'include_dirs':[
									'alsa-lib_config/android',
								]
							}],
							
							['OS in "linux android"',{
								'sources':[
									'alsa-lib_src/src/async.c',
									'alsa-lib_src/src/conf.c',
									'alsa-lib_src/src/confmisc.c',
									'alsa-lib_src/src/dlmisc.c',
									'alsa-lib_src/src/error.c',
									'alsa-lib_src/src/input.c',
									'alsa-lib_src/src/names.c',
									'alsa-lib_src/src/output.c',
									#'alsa-lib_src/src/shmarea.c',
									'alsa-lib_src/src/socket.c',
									'alsa-lib_src/src/userfile.c',
									'alsa-lib_src/src/alisp/alisp.c',
									#'alsa-lib_src/src/alisp/alisp_snd.c',
									#'alsa-lib_src/src/compat/empty.c',
									#'alsa-lib_src/src/compat/hsearch_r.c',
									'alsa-lib_src/src/control/cards.c',
									'alsa-lib_src/src/control/control.c',
									'alsa-lib_src/src/control/control_ext.c',
									'alsa-lib_src/src/control/control_hw.c',
									#'alsa-lib_src/src/control/control_shm.c',
									'alsa-lib_src/src/control/control_symbols.c',
									'alsa-lib_src/src/control/ctlparse.c',
									'alsa-lib_src/src/control/hcontrol.c',
									'alsa-lib_src/src/control/namehint.c',
									'alsa-lib_src/src/control/setup.c',
									'alsa-lib_src/src/control/tlv.c',
									'alsa-lib_src/src/hwdep/hwdep.c',
									'alsa-lib_src/src/hwdep/hwdep_hw.c',
									'alsa-lib_src/src/hwdep/hwdep_symbols.c',
									'alsa-lib_src/src/mixer/bag.c',
									'alsa-lib_src/src/mixer/mixer.c',
									'alsa-lib_src/src/mixer/simple.c',
									'alsa-lib_src/src/mixer/simple_abst.c',
									'alsa-lib_src/src/mixer/simple_none.c',
									'alsa-lib_src/src/pcm/atomic.c',
									'alsa-lib_src/src/pcm/interval.c',
									'alsa-lib_src/src/pcm/mask.c',
									'alsa-lib_src/src/pcm/pcm.c',
									'alsa-lib_src/src/pcm/pcm_adpcm.c',
									'alsa-lib_src/src/pcm/pcm_alaw.c',
									'alsa-lib_src/src/pcm/pcm_asym.c',
									'alsa-lib_src/src/pcm/pcm_copy.c',
									#'alsa-lib_src/src/pcm/pcm_direct.c',
									#'alsa-lib_src/src/pcm/pcm_dmix.c',
									#'alsa-lib_src/src/pcm/pcm_dmix_generic.c',
									#'alsa-lib_src/src/pcm/pcm_dmix_i386.c',
									#'alsa-lib_src/src/pcm/pcm_dmix_x86_64.c',
									#'alsa-lib_src/src/pcm/pcm_dshare.c',
									#'alsa-lib_src/src/pcm/pcm_dsnoop.c',
									'alsa-lib_src/src/pcm/pcm_empty.c',
									'alsa-lib_src/src/pcm/pcm_extplug.c',
									'alsa-lib_src/src/pcm/pcm_file.c',
									'alsa-lib_src/src/pcm/pcm_generic.c',
									'alsa-lib_src/src/pcm/pcm_hooks.c',
									'alsa-lib_src/src/pcm/pcm_hw.c',
									'alsa-lib_src/src/pcm/pcm_iec958.c',
									'alsa-lib_src/src/pcm/pcm_ioplug.c',
									#'alsa-lib_src/src/pcm/pcm_ladspa.c',
									'alsa-lib_src/src/pcm/pcm_lfloat.c',
									'alsa-lib_src/src/pcm/pcm_linear.c',
									'alsa-lib_src/src/pcm/pcm_meter.c',
									'alsa-lib_src/src/pcm/pcm_misc.c',
									'alsa-lib_src/src/pcm/pcm_mmap.c',
									'alsa-lib_src/src/pcm/pcm_mmap_emul.c',
									'alsa-lib_src/src/pcm/pcm_mulaw.c',
									'alsa-lib_src/src/pcm/pcm_multi.c',
									'alsa-lib_src/src/pcm/pcm_null.c',
									'alsa-lib_src/src/pcm/pcm_params.c',
									'alsa-lib_src/src/pcm/pcm_plug.c',
									'alsa-lib_src/src/pcm/pcm_plugin.c',
									'alsa-lib_src/src/pcm/pcm_rate.c',
									'alsa-lib_src/src/pcm/pcm_rate_linear.c',
									'alsa-lib_src/src/pcm/pcm_route.c',
									'alsa-lib_src/src/pcm/pcm_share.c',
									#'alsa-lib_src/src/pcm/pcm_shm.c',
									'alsa-lib_src/src/pcm/pcm_simple.c',
									'alsa-lib_src/src/pcm/pcm_softvol.c',
									'alsa-lib_src/src/pcm/pcm_symbols.c',
									#'alsa-lib_src/src/pcm/scopes/level.c',
									'alsa-lib_src/src/rawmidi/rawmidi.c',
									'alsa-lib_src/src/rawmidi/rawmidi_hw.c',
									'alsa-lib_src/src/rawmidi/rawmidi_symbols.c',
									'alsa-lib_src/src/rawmidi/rawmidi_virt.c',
									'alsa-lib_src/src/seq/seq.c',
									'alsa-lib_src/src/seq/seqmid.c',
									'alsa-lib_src/src/seq/seq_event.c',
									'alsa-lib_src/src/seq/seq_hw.c',
									'alsa-lib_src/src/seq/seq_midi_event.c',
									'alsa-lib_src/src/seq/seq_old.c',
									'alsa-lib_src/src/seq/seq_symbols.c',
									'alsa-lib_src/src/timer/timer.c',
									'alsa-lib_src/src/timer/timer_hw.c',
									'alsa-lib_src/src/timer/timer_query.c',
									'alsa-lib_src/src/timer/timer_query_hw.c',
									'alsa-lib_src/src/timer/timer_symbols.c',
									'alsa-lib_src/src/ucm/main.c',
									'alsa-lib_src/src/ucm/parser.c',
									'alsa-lib_src/src/ucm/utils.c',
								],
							}],
							
						],
					}],

					['alsa_lib_type == "salsa"',{
						'include_dirs':[
							'salsa-lib_src/src',
							'salsa_config',
						],
						'defines':[
							#'__SALSA_EXPORT_FUNC',
						],
						'direct_dependent_settings': {
							'include_dirs': [
								'includes',
								'salsa_config',
							],
						 },
						'copies':[
							{
								'destination':'includes/alsa',
								'files':[
									'salsa_config/asoundlib.h',
									#'salsa-lib_src/src/asoundlib.h',
									'salsa_config/version.h',
									'salsa_config/recipe.h',
									'salsa-lib_src/src/asoundef.h',
									'salsa-lib_src/src/asound.h',
									'salsa-lib_src/src/ctl_func.h',
									'salsa-lib_src/src/ctl_macros.h',
									'salsa-lib_src/src/global.h',
									'salsa-lib_src/src/input.h',
									'salsa-lib_src/src/output.h',
									'salsa-lib_src/src/error.h',
									'salsa-lib_src/src/conf.h',
									'salsa-lib_src/src/pcm.h',
									'salsa-lib_src/src/pcm_func.h',
									'salsa-lib_src/src/pcm_macros.h',
									'salsa-lib_src/src/rawmidi.h',
									'salsa-lib_src/src/timer.h',
									'salsa-lib_src/src/timer_func.h',
									'salsa-lib_src/src/timer_macros.h',
									'salsa-lib_src/src/hwdep.h',
									'salsa-lib_src/src/hwdep_func.h',
									'salsa-lib_src/src/hwdep_macros.h',
									'salsa-lib_src/src/hcontrol.h',
									'salsa-lib_src/src/hctl_func.h',
									'salsa-lib_src/src/hctl_macros.h',
									'salsa-lib_src/src/control.h',
									'salsa-lib_src/src/mixer.h',
									'salsa-lib_src/src/mixer_func.h',
									'salsa-lib_src/src/mixer_macros.h',
									'salsa-lib_src/src/seq_event.h',
									'salsa-lib_src/src/seq.h',
									'salsa-lib_src/src/seqmid.h',
									'salsa-lib_src/src/rawmidi_func.h',
									'salsa-lib_src/src/rawmidi_macros.h',
									#'salsa-lib_src/src/seq_midi_event.h',
								],
							},
						],
						
						'sources' : [],
						'conditions':[
							['OS in "linux android"',{
								'sources':[
									'salsa-lib_src/src/asound.h',
									'salsa-lib_src/src/asoundef.h',
									'salsa-lib_src/src/asoundlib-head.h',
									'salsa-lib_src/src/asoundlib-tail.h',
									'salsa-lib_src/src/async.c',
									'salsa-lib_src/src/cards.c',
									'salsa-lib_src/src/conf.h',
									'salsa-lib_src/src/conf_abi.c',
									'salsa-lib_src/src/control.c',
									'salsa-lib_src/src/control.h',
									'salsa-lib_src/src/ctl_abi.c',
									'salsa-lib_src/src/ctl_func.h',
									'salsa-lib_src/src/ctl_macros.h',
									'salsa-lib_src/src/error.h',
									'salsa-lib_src/src/error_abi.c',
									'salsa-lib_src/src/global.h',
									'salsa-lib_src/src/global_abi.c',
									'salsa-lib_src/src/hcontrol.c',
									'salsa-lib_src/src/hcontrol.h',
									'salsa-lib_src/src/hctl_abi.c',
									'salsa-lib_src/src/hctl_func.h',
									'salsa-lib_src/src/hctl_macros.h',
									'salsa-lib_src/src/hwdep.c',
									'salsa-lib_src/src/hwdep.h',
									'salsa-lib_src/src/hwdep_abi.c',
									'salsa-lib_src/src/hwdep_func.h',
									'salsa-lib_src/src/hwdep_macros.h',
									'salsa-lib_src/src/input.h',
									'salsa-lib_src/src/input_abi.c',
									'salsa-lib_src/src/local.h',
									'salsa-lib_src/src/mixer.c',
									'salsa-lib_src/src/mixer.h',
									'salsa-lib_src/src/mixer_abi.c',
									'salsa-lib_src/src/mixer_func.h',
									'salsa-lib_src/src/mixer_macros.h',
									'salsa-lib_src/src/output.h',
									'salsa-lib_src/src/output_abi.c',
									'salsa-lib_src/src/pcm.c',
									'salsa-lib_src/src/pcm.h',
									'salsa-lib_src/src/pcm_abi.c',
									'salsa-lib_src/src/pcm_func.h',
									'salsa-lib_src/src/pcm_macros.h',
									'salsa-lib_src/src/pcm_misc.c',
									'salsa-lib_src/src/pcm_params.c',
									'salsa-lib_src/src/rawmidi.c',
									'salsa-lib_src/src/rawmidi.h',
									'salsa-lib_src/src/rawmidi_abi.c',
									'salsa-lib_src/src/rawmidi_func.h',
									'salsa-lib_src/src/rawmidi_macros.h',
									'salsa-lib_src/src/seq.h',
									'salsa-lib_src/src/seqmid.h',
									'salsa-lib_src/src/seq_event.h',
									'salsa-lib_src/src/timer.c',
									'salsa-lib_src/src/timer.h',
									'salsa-lib_src/src/timer_abi.c',
									'salsa-lib_src/src/timer_func.h',
									'salsa-lib_src/src/timer_macros.h',

									'salsa_config/version.h',
									'salsa_config/recipe.h',
								],
							}],
						],

					}],
						
				],
			},
		],
					
	  
	
}