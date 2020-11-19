import unittest

from vmaf.core.asset import Asset

from vmaf.config import VmafConfig

from test.testutil import set_default_576_324_videos_for_testing, \
    set_default_576_324_12bit_videos_for_testing, \
    set_default_576_324_16bit_videos_for_testing, \
    set_default_576_324_10bit_videos_for_testing_b, \
    set_default_576_324_10bit_videos_for_testing

from vmaf.core.vmafrc_feature_extractor import FloatMotionFeatureExtractor, IntegerMotionFeatureExtractor, \
    FloatVifFeatureExtractor, FloatAdmFeatureExtractor, IntegerVifFeatureExtractor, IntegerPsnrFeatureExtractor, \
    IntegerAdmFeatureExtractor


class FeatureExtractorTest(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.maxDiff = None

    def tearDown(self):
        if hasattr(self, 'fextractor'):
            self.fextractor.remove_results()
        pass
        self.assertEqual([], self.verificationErrors)

    def test_run_float_motion_fextractor(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_videos_for_testing()
        self.fextractor = FloatMotionFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['float_motion_feature_motion2_score'], 3.8953518541666665, places=8)
        self.assertAlmostEqual(results[1]['float_motion_feature_motion2_score'], 3.8953518541666665, places=8)

    def test_run_float_motion_fextractor_forcing_zero(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_videos_for_testing()
        self.fextractor = FloatMotionFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None,
            optional_dict={'motion_force_zero': True},
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['float_motion_feature_motion2_score'], 0.0, places=8)
        self.assertAlmostEqual(results[1]['float_motion_feature_motion2_score'], 0.0, places=8)

        self.assertEqual(len(results[0]['float_motion_feature_motion2_scores']), 48)
        self.assertEqual(len(results[1]['float_motion_feature_motion2_scores']), 48)

    def test_run_integer_motion_fextractor(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_videos_for_testing()
        self.fextractor = IntegerMotionFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_motion_feature_motion2_score'], 3.895345229166667, places=8)
        self.assertAlmostEqual(results[1]['integer_motion_feature_motion2_score'], 3.895345229166667, places=8)

    def test_run_integer_motion_fextractor_forcing_zero(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_videos_for_testing()
        self.fextractor = IntegerMotionFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None,
            optional_dict={'motion_force_zero': True}
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_motion_feature_motion2_score'], 0.0, places=8)
        self.assertAlmostEqual(results[1]['integer_motion_feature_motion2_score'], 0.0, places=8)

    def test_run_integer_motion_fextractor_12bit(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_12bit_videos_for_testing()
        self.fextractor = IntegerMotionFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_motion_feature_motion2_score'], 2.8104533333333332, places=8)
        self.assertAlmostEqual(results[1]['integer_motion_feature_motion2_score'], 2.8104533333333332, places=8)

    def test_run_float_vif_fextractor(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_videos_for_testing()
        self.fextractor = FloatVifFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale0_score'], 0.3634208125, places=6)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale1_score'], 0.7666474166666667, places=6)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale2_score'], 0.8628533333333334, places=6)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale3_score'], 0.9159719583333334, places=6)
        self.assertAlmostEqual(results[1]['float_VIF_feature_vif_scale0_score'], 1.0, places=6)
        self.assertAlmostEqual(results[1]['float_VIF_feature_vif_scale1_score'], 1.0, places=6)
        self.assertAlmostEqual(results[1]['float_VIF_feature_vif_scale2_score'], 1.0, places=6)
        self.assertAlmostEqual(results[1]['float_VIF_feature_vif_scale3_score'], 1.0, places=5)

    def test_run_integer_vif_fextractor(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_videos_for_testing()
        self.fextractor = IntegerVifFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale0_score'], 0.3636620625, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale1_score'], 0.7674953125, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale2_score'], 0.8631078125, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale3_score'], 0.9157200833333333, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[1]['integer_VIF_feature_vif_scale0_score'], 1.0, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[1]['integer_VIF_feature_vif_scale1_score'], 1.0, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[1]['integer_VIF_feature_vif_scale2_score'], 1.0, places=5)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[1]['integer_VIF_feature_vif_scale3_score'], 1.0, places=5)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_run_integer_vif_fextractor_12bit(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_12bit_videos_for_testing()
        self.fextractor = IntegerVifFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale0_score'], 0.4330893333333334, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale1_score'], 0.830613, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale2_score'], 0.9072123333333333, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale3_score'], 0.945896, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[1]['integer_VIF_feature_vif_scale0_score'], 1.0, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[1]['integer_VIF_feature_vif_scale1_score'], 1.0, places=6)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[1]['integer_VIF_feature_vif_scale2_score'], 1.0, places=5)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[1]['integer_VIF_feature_vif_scale3_score'], 1.0, places=5)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_run_integer_vif_fextractor_debug1_yuv422p10le(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_10bit_videos_for_testing()
        self.fextractor = IntegerVifFeatureExtractor(
            [asset],
            None, fifo_mode=True,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale0_scores'][-1], 0.416114, places=6)

    def test_run_integer_vif_fextractor_debug2_160x90(self):
        ref_path = VmafConfig.test_resource_path("yuv", "ref_test_0_1_src01_hrc00_576x324_576x324_vs_src01_hrc01_576x324_576x324_q_160x90.yuv")
        dis_path = VmafConfig.test_resource_path("yuv", "dis_test_0_1_src01_hrc00_576x324_576x324_vs_src01_hrc01_576x324_576x324_q_160x90.yuv")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 160, 'height': 90})
        self.fextractor = IntegerVifFeatureExtractor(
            [asset],
            None, fifo_mode=True,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale3_scores'][31], 0.983114, places=6)

    def test_run_integer_vif_fextractor_debug3_yuv420p10le(self):
        ref_path = VmafConfig.test_resource_path("yuv", "sparks_ref_480x270.yuv42010le.yuv")
        dis_path = VmafConfig.test_resource_path("yuv", "sparks_dis_480x270.yuv42010le.yuv")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 480, 'height': 270,
                                  'yuv_type': 'yuv420p10le'})
        self.fextractor = IntegerVifFeatureExtractor(
            [asset],
            None, fifo_mode=True,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale0_scores'][0], 0.933165, places=6)
        self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale3_scores'][2], 0.999352, places=6)

    def test_run_float_adm_fextractor(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_videos_for_testing()
        self.fextractor = FloatAdmFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['float_ADM_feature_adm2_score'], 0.9345148541666667, places=4)
        self.assertAlmostEqual(results[1]['float_ADM_feature_adm2_score'], 1.0, places=6)

    def test_run_integer_psnr_fextractor(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_videos_for_testing()
        self.fextractor = IntegerPsnrFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_PSNR_feature_psnr_y_score'], 30.755063979166664, places=4)
        self.assertAlmostEqual(results[0]['integer_PSNR_feature_psnr_cb_score'], 38.4494410625, places=4)
        self.assertAlmostEqual(results[0]['integer_PSNR_feature_psnr_cr_score'], 40.99191027083334, places=4)
        self.assertAlmostEqual(results[1]['integer_PSNR_feature_psnr_y_score'], 60.0, places=4)
        self.assertAlmostEqual(results[1]['integer_PSNR_feature_psnr_cb_score'], 60.0, places=4)
        self.assertAlmostEqual(results[1]['integer_PSNR_feature_psnr_cr_score'], 60.0, places=4)

    def test_run_integer_psnr_fextractor_12bit(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_12bit_videos_for_testing()
        self.fextractor = IntegerPsnrFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_PSNR_feature_psnr_y_score'], 32.577818, places=4)
        self.assertAlmostEqual(results[0]['integer_PSNR_feature_psnr_cb_score'], 39.044961, places=4)
        self.assertAlmostEqual(results[0]['integer_PSNR_feature_psnr_cr_score'], 41.286965333333335, places=4)
        self.assertAlmostEqual(results[1]['integer_PSNR_feature_psnr_y_score'], 84.0, places=4)
        self.assertAlmostEqual(results[1]['integer_PSNR_feature_psnr_cb_score'], 84.0, places=4)
        self.assertAlmostEqual(results[1]['integer_PSNR_feature_psnr_cr_score'], 84.0, places=4)

    def test_run_integer_psnr_fextractor_16bit(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_16bit_videos_for_testing()
        self.fextractor = IntegerPsnrFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_PSNR_feature_psnr_y_score'], 32.579806000000005, places=4)
        self.assertAlmostEqual(results[0]['integer_PSNR_feature_psnr_cb_score'], 39.04694966666667, places=4)
        self.assertAlmostEqual(results[0]['integer_PSNR_feature_psnr_cr_score'], 41.288954, places=4)
        self.assertAlmostEqual(results[1]['integer_PSNR_feature_psnr_y_score'], 108.0, places=4)
        self.assertAlmostEqual(results[1]['integer_PSNR_feature_psnr_cb_score'], 108.0, places=4)
        self.assertAlmostEqual(results[1]['integer_PSNR_feature_psnr_cr_score'], 108.0, places=4)

    def test_run_float_adm_fextractor_akiyo_multiply(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = FloatAdmFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['float_ADM_feature_adm2_score'], 1.116686, places=6)

    def test_run_float_adm_fextractor_akiyo_multiply_enhn_gain_limit_1(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = FloatAdmFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None,
            optional_dict={'adm_enhn_gain_limit': 1.0}
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['float_ADM_feature_adm2_score'], 0.9574308606115118, places=6)

    def test_run_float_adm_fextractor_akiyo_multiply_enhn_gain_limit_1d2(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = FloatAdmFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None,
            optional_dict={'adm_enhn_gain_limit': 1.2}
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['float_ADM_feature_adm2_score'], 1.116595, places=6)

    def test_run_float_vif_fextractor_akiyo_multiply(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = FloatVifFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale0_score'], 1.0522544319369052, places=5)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale1_score'], 1.0705609423182443, places=5)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale2_score'], 1.0731529493098957, places=5)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale3_score'], 1.0728060231246508, places=5)

    def test_run_float_vif_fextractor_akiyo_multiply_enhn_gain_limit_1(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = FloatVifFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None,
            optional_dict={'vif_enhn_gain_limit': 1.0},
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale0_score'], 0.983699512450884, places=4)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale1_score'], 0.9974276726830457, places=4)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale2_score'], 0.9984692380091739, places=4)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale3_score'], 0.999146211879154, places=4)

    def test_run_float_vif_fextractor_akiyo_multiply_enhn_gain_limit_1d1(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = FloatVifFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None,
            optional_dict={'vif_enhn_gain_limit': 1.1},
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale0_score'], 1.0298451531242514, places=3)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale1_score'], 1.046596975760772, places=3)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale2_score'], 1.0485607628500504, places=3)
        self.assertAlmostEqual(results[0]['float_VIF_feature_vif_scale3_score'], 1.0491232394147363, places=3)

    def test_run_integer_vif_fextractor_akiyo_multiply(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = IntegerVifFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale0_score'], 1.052403, places=5)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale1_score'], 1.070149, places=5)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale2_score'], 1.072518, places=5)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale3_score'], 1.072512, places=5)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_run_integer_vif_fextractor_akiyo_multiply_enhn_gain_limit_1(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = IntegerVifFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None,
            optional_dict={'vif_enhn_gain_limit': 1.0},
        )
        self.fextractor.run()
        results = self.fextractor.results
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale0_score'], 0.983699512450884, places=4)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale1_score'], 0.9974276726830457, places=4)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale2_score'], 0.9984692380091739, places=4)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale3_score'], 0.999146211879154, places=4)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_run_integer_vif_fextractor_akiyo_multiply_enhn_gain_limit_1d1(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = IntegerVifFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None,
            optional_dict={'vif_enhn_gain_limit': 1.1},
        )
        self.fextractor.run()
        results = self.fextractor.results
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale0_score'], 1.0298451531242514, places=3)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale1_score'], 1.046596975760772, places=3)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale2_score'], 1.0485607628500504, places=3)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertAlmostEqual(results[0]['integer_VIF_feature_vif_scale3_score'], 1.0491232394147363, places=3)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_run_integer_adm_fextractor(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_videos_for_testing()
        self.fextractor = IntegerAdmFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_ADM_feature_adm2_score'], 0.9345057916666667, places=4)
        self.assertAlmostEqual(results[1]['integer_ADM_feature_adm2_score'], 1.000002, places=6)

    def test_run_integer_adm_fextractor_12bit(self):
        ref_path, dis_path, asset, asset_original = set_default_576_324_12bit_videos_for_testing()
        self.fextractor = IntegerAdmFeatureExtractor(
            [asset, asset_original],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_ADM_feature_adm2_score'], 0.9517706666666667, places=4)
        self.assertAlmostEqual(results[1]['integer_ADM_feature_adm2_score'], 1.000002, places=6)

    def test_run_integer_adm_fextractor_akiyo_multiply(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = IntegerAdmFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_ADM_feature_adm2_score'], 1.1167, places=6)  # float 1.116686

    def test_run_integer_adm_fextractor_akiyo_multiply_enhn_gain_limit_1(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = IntegerAdmFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None,
            optional_dict={'adm_enhn_gain_limit': 1.0}
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_ADM_feature_adm2_score'], 0.957433, places=6)  # float 0.9574308606115118

    def test_run_integer_adm_fextractor_akiyo_multiply_enhn_gain_limit_1d2(self):
        ref_path = VmafConfig.test_resource_path("yuv", "refp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        dis_path = VmafConfig.test_resource_path("yuv", "disp_vmaf_hacking_investigation_0_0_akiyo_cif_notyuv_0to0_identity_vs_akiyo_cif_notyuv_0to0_multiply_q_352x288")
        asset = Asset(dataset="test", content_id=0, asset_id=0,
                      workdir_root=VmafConfig.workdir_path(),
                      ref_path=ref_path,
                      dis_path=dis_path,
                      asset_dict={'width': 352, 'height': 288})
        self.fextractor = IntegerAdmFeatureExtractor(
            [asset],
            None, fifo_mode=False,
            result_store=None,
            optional_dict={'adm_enhn_gain_limit': 1.2}
        )
        self.fextractor.run()
        results = self.fextractor.results
        self.assertAlmostEqual(results[0]['integer_ADM_feature_adm2_score'], 1.116609, places=6)  # float 1.116595


if __name__ == '__main__':
    unittest.main(verbosity=2)
