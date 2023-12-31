# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/nbi/v1alpha/resources/network_link.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common import control_radio_pb2 as api_dot_common_dot_control__radio__pb2
from api.common import coordinates_pb2 as api_dot_common_dot_coordinates__pb2
from api.common import network_pb2 as api_dot_common_dot_network__pb2
from api.common import time_pb2 as api_dot_common_dot_time__pb2
from api.common import wireless_transceiver_pb2 as api_dot_common_dot_wireless__transceiver__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,api/nbi/v1alpha/resources/network_link.proto\x12+aalyria.spacetime.api.nbi.v1alpha.resources\x1a\x1e\x61pi/common/control_radio.proto\x1a\x1c\x61pi/common/coordinates.proto\x1a\x18\x61pi/common/network.proto\x1a\x15\x61pi/common/time.proto\x1a%api/common/wireless_transceiver.proto\"\xa1\x01\n\x0bNetworkLink\x12\x42\n\x03src\x18\x03 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.NetworkInterfaceIdR\x03src\x12\x42\n\x03\x64st\x18\x04 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.NetworkInterfaceIdR\x03\x64stJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"\xfb\x02\n\x12RadioConfiguration\x12S\n\x0cinterface_id\x18\x01 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.NetworkInterfaceIdR\x0binterfaceId\x12I\n\x08tx_state\x18\x02 \x01(\x0b\x32..aalyria.spacetime.api.common.TransmitterStateR\x07txState\x12\x46\n\x08rx_state\x18\x03 \x01(\x0b\x32+.aalyria.spacetime.api.common.ReceiverStateR\x07rxState\x12\"\n\rrate_table_id\x18\x05 \x01(\tR\x0brateTableId\x12O\n\rtdma_schedule\x18\x04 \x01(\x0b\x32*.aalyria.spacetime.api.common.TdmaScheduleR\x0ctdmaScheduleJ\x08\x08\x06\x10\x80\x80\x80\x80\x02\"_\n\x05Radio\x12.\n\x13\x63\x65nter_frequency_hz\x18\x01 \x01(\x04R\x11\x63\x65nterFrequencyHz\x12&\n\x0f\x62\x61nd_profile_id\x18\x02 \x01(\tR\rbandProfileId\"]\n\x07LinkEnd\x12@\n\x02id\x18\x03 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.NetworkInterfaceIdR\x02idJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x04\x10\x05\"\xb9\x01\n\nBeamTarget\x12Y\n\x0etransceiver_id\x18\x01 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.TransceiverModelIdH\x00R\rtransceiverId\x12H\n\x0b\x63oordinates\x18\x02 \x01(\x0b\x32$.aalyria.spacetime.api.common.MotionH\x00R\x0b\x63oordinatesB\x06\n\x04type\"\xc5\x02\n\x11\x42idirectionalLink\x12\x42\n\x01\x61\x18\x01 \x01(\x0b\x32\x34.aalyria.spacetime.api.nbi.v1alpha.resources.LinkEndR\x01\x61\x12\x42\n\x01\x62\x18\x02 \x01(\x0b\x32\x34.aalyria.spacetime.api.nbi.v1alpha.resources.LinkEndR\x01\x62\x12S\n\x0c\x61_to_b_radio\x18\x03 \x01(\x0b\x32\x32.aalyria.spacetime.api.nbi.v1alpha.resources.RadioR\taToBRadio\x12S\n\x0c\x62_to_a_radio\x18\x04 \x01(\x0b\x32\x32.aalyria.spacetime.api.nbi.v1alpha.resources.RadioR\tbToARadio\"\x89\x02\n\x0f\x44irectionalLink\x12@\n\x02id\x18\x01 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.NetworkInterfaceIdR\x02id\x12\x63\n\x13radio_configuration\x18\x02 \x01(\x0b\x32\x32.aalyria.spacetime.api.nbi.v1alpha.resources.RadioR\x12radioConfiguration\x12O\n\x06target\x18\x03 \x01(\x0b\x32\x37.aalyria.spacetime.api.nbi.v1alpha.resources.BeamTargetR\x06target\"\xf4\x07\n\x12WirelessLinkBudget\x12^\n-transmitter_antenna_gain_in_link_direction_db\x18\x01 \x01(\x01R\'transmitterAntennaGainInLinkDirectionDb\x12R\n&effective_isotropic_radiated_power_dbw\x18\x02 \x01(\x01R\"effectiveIsotropicRadiatedPowerDbw\x12\xa2\x01\n\x1d\x63omponent_propagation_loss_db\x18\x0f \x03(\x0b\x32_.aalyria.spacetime.api.nbi.v1alpha.resources.WirelessLinkBudget.ComponentPropagationLossDbEntryR\x1a\x63omponentPropagationLossDb\x12.\n\x13propagation_loss_db\x18\x03 \x01(\x01R\x11propagationLossDb\x12?\n\x1creceived_isotropic_power_dbw\x18\x04 \x01(\x01R\x19receivedIsotropicPowerDbw\x12Q\n\'received_power_flux_density_db_w_per_m2\x18\x05 \x01(\x01R receivedPowerFluxDensityDbWPerM2\x12X\n*receiver_antenna_gain_in_link_direction_db\x18\x06 \x01(\x01R$receiverAntennaGainInLinkDirectionDb\x12>\n\x1cpower_at_receiver_output_dbw\x18\x07 \x01(\x01R\x18powerAtReceiverOutputDbw\x12-\n\x13\x63\x61rrier_to_noise_db\x18\x08 \x01(\x01R\x10\x63\x61rrierToNoiseDb\x12O\n%carrier_to_noise_plus_interference_db\x18\x10 \x01(\x01R carrierToNoisePlusInterferenceDb\x12H\n\"carrier_to_noise_density_db_per_hz\x18\t \x01(\x01R\x1c\x63\x61rrierToNoiseDensityDbPerHz\x1aM\n\x1f\x43omponentPropagationLossDbEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value:\x02\x38\x01J\x04\x08\n\x10\x0fJ\x08\x08\x11\x10\x80\x80\x80\x80\x02\"\xbe\t\n\x12WirelessLinkReport\x12\x42\n\x03\x64st\x18\x01 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.TransceiverModelIdR\x03\x64st\x12&\n\x0f\x62\x61nd_profile_id\x18\x02 \x01(\tR\rbandProfileId\x12\x32\n\x15\x63\x65nter_frequencies_hz\x18\x03 \x03(\x04R\x13\x63\x65nterFrequenciesHz\x12\x81\x01\n\x10\x61\x63\x63\x65ss_intervals\x18\x04 \x03(\x0b\x32V.aalyria.spacetime.api.nbi.v1alpha.resources.WirelessLinkReport.WirelessAccessIntervalR\x0f\x61\x63\x63\x65ssIntervals\x1a\x83\x07\n\x16WirelessAccessInterval\x12\x46\n\x08interval\x18\x01 \x01(\x0b\x32*.aalyria.spacetime.api.common.TimeIntervalR\x08interval\x12`\n\raccessibility\x18\x02 \x01(\x0e\x32:.aalyria.spacetime.api.nbi.v1alpha.resources.AccessibilityR\raccessibility\x12(\n\x10no_access_reason\x18\x03 \x03(\tR\x0enoAccessReason\x12\x93\x01\n\x0fsampled_metrics\x18\x04 \x03(\x0b\x32j.aalyria.spacetime.api.nbi.v1alpha.resources.WirelessLinkReport.WirelessAccessInterval.WirelessLinkMetricsR\x0esampledMetrics\x1a\xfe\x03\n\x13WirelessLinkMetrics\x12\x44\n\ttimestamp\x18\x01 \x01(\x0b\x32&.aalyria.spacetime.api.common.DateTimeR\ttimestamp\x12S\n\x11propagation_delay\x18\x02 \x01(\x0b\x32&.aalyria.spacetime.api.common.DurationR\x10propagationDelay\x12U\n\x0fpointing_vector\x18\x03 \x01(\x0b\x32,.aalyria.spacetime.api.common.PointingVectorR\x0epointingVector\x12\x17\n\x07range_m\x18\x04 \x01(\x01R\x06rangeM\x12\"\n\rdata_rate_bps\x18\x06 \x01(\x01R\x0b\x64\x61taRateBps\x12^\n-transmitter_antenna_gain_in_link_direction_db\x18\x07 \x01(\x01R\'transmitterAntennaGainInLinkDirectionDb\x12X\n*receiver_antenna_gain_in_link_direction_db\x18\x08 \x01(\x01R$receiverAntennaGainInLinkDirectionDb\"\xd5\x04\n\x13InterfaceLinkReport\x12\x42\n\x03src\x18\x04 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.NetworkInterfaceIdR\x03src\x12\x42\n\x03\x64st\x18\x05 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.NetworkInterfaceIdR\x03\x64st\x12z\n\x10\x61\x63\x63\x65ss_intervals\x18\x06 \x03(\x0b\x32O.aalyria.spacetime.api.nbi.v1alpha.resources.InterfaceLinkReport.AccessIntervalR\x0f\x61\x63\x63\x65ssIntervals\x1a\xa7\x02\n\x0e\x41\x63\x63\x65ssInterval\x12\x46\n\x08interval\x18\x01 \x01(\x0b\x32*.aalyria.spacetime.api.common.TimeIntervalR\x08interval\x12`\n\raccessibility\x18\x02 \x01(\x0e\x32:.aalyria.spacetime.api.nbi.v1alpha.resources.AccessibilityR\raccessibility\x12G\n\x0b\x66rame_delay\x18\x03 \x01(\x0b\x32&.aalyria.spacetime.api.common.DurationR\nframeDelay\x12\"\n\rdata_rate_bps\x18\x04 \x01(\x01R\x0b\x64\x61taRateBpsJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\"\xb2\x01\n\x15TransceiverLinkReport\x12\x42\n\x03src\x18\x01 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.TransceiverModelIdR\x03src\x12U\n\x05links\x18\x02 \x03(\x0b\x32?.aalyria.spacetime.api.nbi.v1alpha.resources.WirelessLinkReportR\x05links*Z\n\rAccessibility\x12\x12\n\x0e\x41\x43\x43\x45SS_UNKNOWN\x10\x00\x12\x11\n\rACCESS_EXISTS\x10\x01\x12\x13\n\x0f\x41\x43\x43\x45SS_MARGINAL\x10\x03\x12\r\n\tNO_ACCESS\x10\x02\x42\x62\n/com.aalyria.spacetime.api.nbi.v1alpha.resourcesZ/aalyria.com/spacetime/api/nbi/v1alpha/resources')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.nbi.v1alpha.resources.network_link_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n/com.aalyria.spacetime.api.nbi.v1alpha.resourcesZ/aalyria.com/spacetime/api/nbi/v1alpha/resources'
  _WIRELESSLINKBUDGET_COMPONENTPROPAGATIONLOSSDBENTRY._options = None
  _WIRELESSLINKBUDGET_COMPONENTPROPAGATIONLOSSDBENTRY._serialized_options = b'8\001'
  _globals['_ACCESSIBILITY']._serialized_start=4778
  _globals['_ACCESSIBILITY']._serialized_end=4868
  _globals['_NETWORKLINK']._serialized_start=244
  _globals['_NETWORKLINK']._serialized_end=405
  _globals['_RADIOCONFIGURATION']._serialized_start=408
  _globals['_RADIOCONFIGURATION']._serialized_end=787
  _globals['_RADIO']._serialized_start=789
  _globals['_RADIO']._serialized_end=884
  _globals['_LINKEND']._serialized_start=886
  _globals['_LINKEND']._serialized_end=979
  _globals['_BEAMTARGET']._serialized_start=982
  _globals['_BEAMTARGET']._serialized_end=1167
  _globals['_BIDIRECTIONALLINK']._serialized_start=1170
  _globals['_BIDIRECTIONALLINK']._serialized_end=1495
  _globals['_DIRECTIONALLINK']._serialized_start=1498
  _globals['_DIRECTIONALLINK']._serialized_end=1763
  _globals['_WIRELESSLINKBUDGET']._serialized_start=1766
  _globals['_WIRELESSLINKBUDGET']._serialized_end=2778
  _globals['_WIRELESSLINKBUDGET_COMPONENTPROPAGATIONLOSSDBENTRY']._serialized_start=2685
  _globals['_WIRELESSLINKBUDGET_COMPONENTPROPAGATIONLOSSDBENTRY']._serialized_end=2762
  _globals['_WIRELESSLINKREPORT']._serialized_start=2781
  _globals['_WIRELESSLINKREPORT']._serialized_end=3995
  _globals['_WIRELESSLINKREPORT_WIRELESSACCESSINTERVAL']._serialized_start=3096
  _globals['_WIRELESSLINKREPORT_WIRELESSACCESSINTERVAL']._serialized_end=3995
  _globals['_WIRELESSLINKREPORT_WIRELESSACCESSINTERVAL_WIRELESSLINKMETRICS']._serialized_start=3485
  _globals['_WIRELESSLINKREPORT_WIRELESSACCESSINTERVAL_WIRELESSLINKMETRICS']._serialized_end=3995
  _globals['_INTERFACELINKREPORT']._serialized_start=3998
  _globals['_INTERFACELINKREPORT']._serialized_end=4595
  _globals['_INTERFACELINKREPORT_ACCESSINTERVAL']._serialized_start=4282
  _globals['_INTERFACELINKREPORT_ACCESSINTERVAL']._serialized_end=4577
  _globals['_TRANSCEIVERLINKREPORT']._serialized_start=4598
  _globals['_TRANSCEIVERLINKREPORT']._serialized_end=4776
# @@protoc_insertion_point(module_scope)
