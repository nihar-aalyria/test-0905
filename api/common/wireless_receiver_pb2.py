# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/common/wireless_receiver.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common import channel_pb2 as api_dot_common_dot_channel__pb2
from api.common import wireless_pb2 as api_dot_common_dot_wireless__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/common/wireless_receiver.proto\x12\x1c\x61\x61lyria.spacetime.api.common\x1a\x18\x61pi/common/channel.proto\x1a\x19\x61pi/common/wireless.proto\"<\n\nRxChannels\x12.\n\x13\x63\x65nter_frequency_hz\x18\x01 \x03(\x03R\x11\x63\x65nterFrequencyHz\"\xec\x03\n\x12ReceiverDefinition\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x61\n\x0b\x63hannel_set\x18\n \x03(\x0b\x32@.aalyria.spacetime.api.common.ReceiverDefinition.ChannelSetEntryR\nchannelSet\x12n\n\x18\x63hannel_selection_method\x18\t \x01(\x0e\x32\x34.aalyria.spacetime.api.common.ChannelSelectionMethodR\x16\x63hannelSelectionMethod\x12j\n\x16signal_processing_step\x18\x0b \x03(\x0b\x32\x34.aalyria.spacetime.api.common.ReceiveSignalProcessorR\x14signalProcessingStep\x1ag\n\x0f\x43hannelSetEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12>\n\x05value\x18\x02 \x01(\x0b\x32(.aalyria.spacetime.api.common.RxChannelsR\x05value:\x02\x38\x01J\x04\x08\x01\x10\x02J\x04\x08\x03\x10\tJ\x04\x08\x0c\x10\rJ\x08\x08\r\x10\x80\x80\x80\x80\x02\"\xe4\x02\n\x16ReceiveSignalProcessor\x12>\n\x06\x66ilter\x18\x01 \x01(\x0b\x32$.aalyria.spacetime.api.common.FilterH\x00R\x06\x66ilter\x12]\n\rphotodetector\x18\x02 \x01(\x0b\x32\x35.aalyria.spacetime.api.common.PhotodetectorDefinitionH\x00R\rphotodetector\x12Q\n\tamplifier\x18\x03 \x01(\x0b\x32\x31.aalyria.spacetime.api.common.AmplifierDefinitionH\x00R\tamplifier\x12P\n\x0cgain_or_loss\x18\x04 \x01(\x0b\x32,.aalyria.spacetime.api.common.MiscGainOrLossH\x00R\ngainOrLossB\x06\n\x04type\"\x81\x04\n\x06\x46ilter\x12!\n\x0c\x66requency_hz\x18\x01 \x01(\x01R\x0b\x66requencyHz\x12\x37\n\x18lower_bandwidth_limit_hz\x18\x02 \x01(\x01R\x15lowerBandwidthLimitHz\x12\x37\n\x18upper_bandwidth_limit_hz\x18\x03 \x01(\x01R\x15upperBandwidthLimitHz\x12.\n\x13noise_temperature_k\x18\x04 \x01(\x01R\x11noiseTemperatureK\x12\x64\n\x0brectangular\x18\x05 \x01(\x0b\x32@.aalyria.spacetime.api.common.Filter.RectangularFilterDefinitionH\x00R\x0brectangular\x12U\n\x06linear\x18\x06 \x01(\x0b\x32;.aalyria.spacetime.api.common.Filter.LinearFilterDefinitionH\x00R\x06linear\x1a\x1d\n\x1bRectangularFilterDefinition\x1aG\n\x16LinearFilterDefinition\x12-\n\x13rejection_db_per_hz\x18\x01 \x01(\x01R\x10rejectionDbPerHzB\r\n\x0b\x66ilter_type\"\x8e\x0b\n\x17PhotodetectorDefinition\x12\x88\x01\n\x14\x61valanche_photodiode\x18\x01 \x01(\x0b\x32S.aalyria.spacetime.api.common.PhotodetectorDefinition.AvalanchePhotodiodeDefinitionH\x00R\x13\x61valanchePhotodiode\x12v\n\x0epin_photodiode\x18\x02 \x01(\x0b\x32M.aalyria.spacetime.api.common.PhotodetectorDefinition.PinPhotodiodeDefinitionH\x00R\rpinPhotodiode\x1a\xcc\x04\n\x1d\x41valanchePhotodiodeDefinition\x12)\n\x11\x66ield_of_view_rad\x18\x01 \x01(\x01R\x0e\x66ieldOfViewRad\x12!\n\x0c\x62\x61ndwidth_hz\x18\x02 \x01(\x01R\x0b\x62\x61ndwidthHz\x12.\n\x13noise_temperature_k\x18\x03 \x01(\x01R\x11noiseTemperatureK\x12-\n\x12\x65\x66\x66iciency_percent\x18\x04 \x01(\x01R\x11\x65\x66\x66iciencyPercent\x12(\n\x10\x64\x61rk_current_amp\x18\x05 \x01(\x01R\x0e\x64\x61rkCurrentAmp\x12,\n\x12load_impedance_ohm\x18\x06 \x01(\x01R\x10loadImpedanceOhm\x12!\n\x0cnoise_factor\x18\x07 \x01(\x01R\x0bnoiseFactor\x12\x17\n\x07gain_db\x18\x08 \x01(\x01R\x06gainDb\x12N\n$optical_bandpass_filter_bandwidth_hz\x18\t \x01(\x01R opticalBandpassFilterBandwidthHz\x12\x32\n\x15sky_spectral_radiance\x18\n \x01(\x01R\x13skySpectralRadiance\x12\x43\n\x1esun_spectral_radiant_emittance\x18\x0b \x01(\x01R\x1bsunSpectralRadiantEmittance\x12!\n\x0cwavelength_m\x18\x0c \x01(\x01R\x0bwavelengthM\x1a\x8a\x04\n\x17PinPhotodiodeDefinition\x12)\n\x11\x66ield_of_view_rad\x18\x01 \x01(\x01R\x0e\x66ieldOfViewRad\x12!\n\x0c\x62\x61ndwidth_hz\x18\x02 \x01(\x01R\x0b\x62\x61ndwidthHz\x12.\n\x13noise_temperature_k\x18\x03 \x01(\x01R\x11noiseTemperatureK\x12-\n\x12\x65\x66\x66iciency_percent\x18\x04 \x01(\x01R\x11\x65\x66\x66iciencyPercent\x12(\n\x10\x64\x61rk_current_amp\x18\x05 \x01(\x01R\x0e\x64\x61rkCurrentAmp\x12,\n\x12load_impedance_ohm\x18\x06 \x01(\x01R\x10loadImpedanceOhm\x12N\n$optical_bandpass_filter_bandwidth_hz\x18\x07 \x01(\x01R opticalBandpassFilterBandwidthHz\x12\x32\n\x15sky_spectral_radiance\x18\x08 \x01(\x01R\x13skySpectralRadiance\x12\x43\n\x1esun_spectral_radiant_emittance\x18\t \x01(\x01R\x1bsunSpectralRadiantEmittance\x12!\n\x0cwavelength_m\x18\n \x01(\x01R\x0bwavelengthMB\x14\n\x12photodetector_typeBD\n com.aalyria.spacetime.api.commonZ aalyria.com/spacetime/api/common')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.common.wireless_receiver_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.aalyria.spacetime.api.commonZ aalyria.com/spacetime/api/common'
  _RECEIVERDEFINITION_CHANNELSETENTRY._options = None
  _RECEIVERDEFINITION_CHANNELSETENTRY._serialized_options = b'8\001'
  _globals['_RXCHANNELS']._serialized_start=121
  _globals['_RXCHANNELS']._serialized_end=181
  _globals['_RECEIVERDEFINITION']._serialized_start=184
  _globals['_RECEIVERDEFINITION']._serialized_end=676
  _globals['_RECEIVERDEFINITION_CHANNELSETENTRY']._serialized_start=545
  _globals['_RECEIVERDEFINITION_CHANNELSETENTRY']._serialized_end=648
  _globals['_RECEIVESIGNALPROCESSOR']._serialized_start=679
  _globals['_RECEIVESIGNALPROCESSOR']._serialized_end=1035
  _globals['_FILTER']._serialized_start=1038
  _globals['_FILTER']._serialized_end=1551
  _globals['_FILTER_RECTANGULARFILTERDEFINITION']._serialized_start=1434
  _globals['_FILTER_RECTANGULARFILTERDEFINITION']._serialized_end=1463
  _globals['_FILTER_LINEARFILTERDEFINITION']._serialized_start=1465
  _globals['_FILTER_LINEARFILTERDEFINITION']._serialized_end=1536
  _globals['_PHOTODETECTORDEFINITION']._serialized_start=1554
  _globals['_PHOTODETECTORDEFINITION']._serialized_end=2976
  _globals['_PHOTODETECTORDEFINITION_AVALANCHEPHOTODIODEDEFINITION']._serialized_start=1841
  _globals['_PHOTODETECTORDEFINITION_AVALANCHEPHOTODIODEDEFINITION']._serialized_end=2429
  _globals['_PHOTODETECTORDEFINITION_PINPHOTODIODEDEFINITION']._serialized_start=2432
  _globals['_PHOTODETECTORDEFINITION_PINPHOTODIODEDEFINITION']._serialized_end=2954
# @@protoc_insertion_point(module_scope)
