# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/acd.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/commons/acd.proto\x12\x0b\x61pi.commons\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe0\x01\n\x0c\x41gentSession\x12\x1b\n\tagent_sid\x18\x01 \x01(\x03R\x08\x61gentSid\x12\x1d\n\ntenant_sid\x18\x02 \x01(\x03R\ttenantSid\x12\x1f\n\x0bsession_sid\x18\x03 \x01(\x03R\nsessionSid\x12&\n\x0f\x61sm_session_sid\x18\x04 \x01(\x03R\rasmSessionSid\x12\x15\n\x06org_id\x18\x05 \x01(\tR\x05orgId\x12\x1b\n\tregion_id\x18\x06 \x01(\tR\x08regionId\x12\x17\n\x07user_id\x18\x08 \x01(\tR\x06userId\"\x90\x01\n\tCallerSid\x12\x1d\n\ncaller_sid\x18\x01 \x01(\x03R\tcallerSid\x12.\n\x04type\x18\x02 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x04type\x12\x1d\n\ntenant_sid\x18\x03 \x01(\x03R\ttenantSid\x12\x15\n\x06org_id\x18\x04 \x01(\tR\x05orgId\"\xc1\x08\n\x0b\x41gentStatus\"\xb1\x08\n\x04\x45num\x12\x0f\n\x0bUNAVALIABLE\x10\x00\x12\x08\n\x04IDLE\x10\x01\x12\t\n\x05READY\x10\x02\x12\n\n\x06HUNGUP\x10\x03\x12\r\n\tDESTROYED\x10\x04\x12\n\n\x06PEERED\x10\x05\x12\n\n\x06PAUSED\x10\x06\x12\n\n\x06WRAPUP\x10\x07\x12\x18\n\x14PREPARING_AFTER_IDLE\x10\x08\x12\x1a\n\x16PREPARING_AFTER_WRAPUP\x10\t\x12\x19\n\x15PREPARING_AFTER_PAUSE\x10\n\x12\x1f\n\x1bPREPARING_AFTER_DIAL_CANCEL\x10\x0b\x12\x1e\n\x1aPREPARING_AFTER_PBX_REJECT\x10\x0c\x12\x1e\n\x1aPREPARING_AFTER_PBX_HANGUP\x10\r\x12!\n\x1dPREPARING_AFTER_PBX_WAS_TAKEN\x10\x0e\x12\x1c\n\x18PREPARING_AFTER_GUI_BUSY\x10\x0f\x12\x18\n\x14MANUAL_DIAL_PREPARED\x10\x10\x12\x19\n\x15PREVIEW_DIAL_PREPARED\x10\x11\x12\x17\n\x13MANUAL_DIAL_STARTED\x10\x12\x12\x18\n\x14PREVIEW_DIAL_STARTED\x10\x13\x12\x13\n\x0fOUTBOUND_LOCKED\x10\x14\x12&\n\"WARM_AGENT_TRANSFER_STARTED_SOURCE\x10\x15\x12+\n\'WARM_AGENT_TRANSFER_STARTED_DESTINATION\x10\x16\x12\"\n\x1eWARM_OUTBOUND_TRANSFER_STARTED\x10\x17\x12$\n WARM_OUTBOUND_TRANSFER_PEER_LOST\x10\x18\x12\x14\n\x10PBX_POPUP_LOCKED\x10\x19\x12\x1c\n\x18PEERED_WITH_CALL_ON_HOLD\x10\x1a\x12\x15\n\x11\x43\x41LLBACK_RESUMING\x10\x1b\x12\x0c\n\x08GUI_BUSY\x10\x1c\x12\x0c\n\x08INTERCOM\x10\x1d\x12\x1b\n\x17INTERCOM_RINGING_SOURCE\x10\x1e\x12 \n\x1cINTERCOM_RINGING_DESTINATION\x10\x1f\x12(\n$WARM_OUTBOUND_TRANSFER_OUTBOUND_LOST\x10 \x12\x14\n\x10PREPARED_TO_PEER\x10!\x12&\n\"WARM_SKILL_TRANSFER_SOURCE_PENDING\x10\"\x12\x1b\n\x17\x43\x41LLER_TRANSFER_STARTED\x10#\x12\x1d\n\x19\x43\x41LLER_TRANSFER_LOST_PEER\x10$\x12&\n\"CALLER_TRANSFER_LOST_MERGED_CALLER\x10%\x12\"\n\x1e\x43OLD_OUTBOUND_TRANSFER_STARTED\x10&\x12\x1f\n\x1b\x43OLD_AGENT_TRANSFER_STARTED\x10\'\"\xd9\x03\n\x0c\x43\x61llerStatus\"\xc8\x03\n\x04\x45num\x12\x0f\n\x0bUNAVALIABLE\x10\x00\x12\x08\n\x04IDLE\x10\x01\x12\t\n\x05READY\x10\x02\x12\n\n\x06HUNGUP\x10\x03\x12\r\n\tDESTROYED\x10\x04\x12\n\n\x06PEERED\x10\x05\x12\x13\n\x0fOUTBOUND_LOCKED\x10\x06\x12\x13\n\x0fOUTBOUND_PEERED\x10\x07\x12\x14\n\x10PBX_POPUP_LOCKED\x10\x08\x12\r\n\tVOICEMAIL\x10\t\x12\x1c\n\x18PEERED_WITH_CALL_ON_HOLD\x10\n\x12\x16\n\x12\x43\x41LLBACK_SUSPENDED\x10\x0b\x12\x1f\n\x1bWARM_AGENT_TRANSFER_STARTED\x10\x0c\x12\"\n\x1eWARM_OUTBOUND_TRANSFER_STARTED\x10\r\x12\"\n\x1eOUTBOUND_DIAL_TRANSFER_STARTED\x10\x0e\x12\x14\n\x10PREPARED_TO_PEER\x10\x0f\x12\x1f\n\x1bWARM_SKILL_TRANSFER_PENDING\x10\x10\x12\x18\n\x14\x43\x41LLER_TRANSFER_PEER\x10\x11\x12!\n\x1d\x43\x41LLER_TRANSFER_MERGED_CALLER\x10\x12\x12\x11\n\rCALLER_PEERED\x10\x13\"O\n\x08\x43\x61llType\"C\n\x04\x45num\x12\x0b\n\x07INBOUND\x10\x00\x12\x0c\n\x08OUTBOUND\x10\x01\x12\x0b\n\x07PREVIEW\x10\x02\x12\n\n\x06MANUAL\x10\x03\x12\x07\n\x03MAC\x10\x04\">\n\x0b\x41gentDialIn\"/\n\x04\x45num\x12\r\n\tTOLL_FREE\x10\x00\x12\r\n\tSOFTPHONE\x10\x01\x12\t\n\x05LOCAL\x10\x02\"F\n\rHuntGroupType\"5\n\x04\x45num\x12\x0f\n\x0bUNCONNECTED\x10\x00\x12\r\n\tCONNECTED\x10\x01\x12\r\n\tSOFTPHONE\x10\x02\"\x9b\r\n\x18\x41gentSessionLogActionKey\"\xfe\x0c\n\x04\x45num\x12\x15\n\x11\x41GENT_PAUSE_START\x10\x00\x12\x14\n\x10\x41GENT_PAUSE_STOP\x10\x01\x12\x18\n\x14\x41GENT_SKILLS_INITIAL\x10\x02\x12\x10\n\x0c\x41GENT_LOGOUT\x10\x03\x12\x1a\n\x16\x45XECUTED_AGENT_TRIGGER\x10\x04\x12\x1d\n\x19\x44URATION_SINCE_LAST_LOGON\x10\x05\x12\x12\n\x0e\x41GENT_LOGIN_IP\x10\x06\x12\x10\n\x0cMAC_DECISION\x10\x07\x12\x17\n\x13MAC_10_KEY_DECISION\x10\x08\x12\x16\n\x12MAC_10_KEY_CONFIRM\x10\t\x12\x1b\n\x17HUNT_GROUP_REASSIGNMENT\x10\n\x12\x0e\n\nPBX_ACCEPT\x10\x0b\x12\x0e\n\nPBX_HANGUP\x10\x0c\x12\x0c\n\x08PBX_LOST\x10\r\x12\x0e\n\nPBX_REJECT\x10\x0e\x12\x0f\n\x0bPBX_TIMEOUT\x10\x0f\x12-\n)WARM_TRANSFER_AGENT_INVITE_CALLER_INITIAL\x10\x10\x12%\n!WARM_TRANSFER_AGENT_INVITE_CALLER\x10\x11\x12$\n WARM_TRANSFER_AGENT_START_SOURCE\x10\x12\x12\"\n\x1eWARM_TRANSFER_AGENT_END_SOURCE\x10\x13\x12)\n%WARM_TRANSFER_AGENT_START_DESTINATION\x10\x14\x12\'\n#WARM_TRANSFER_AGENT_END_DESTINATION\x10\x15\x12\x30\n,WARM_TRANSFER_OUTBOUND_INVITE_CALLER_INITIAL\x10\x16\x12(\n$WARM_TRANSFER_OUTBOUND_INVITE_CALLER\x10\x17\x12 \n\x1cWARM_TRANSFER_OUTBOUND_START\x10\x18\x12\x1e\n\x1aWARM_TRANSFER_OUTBOUND_END\x10\x19\x12 \n\x1c\x43OLD_TRANSFER_OUTBOUND_START\x10\x1a\x12$\n COLD_TRANSFER_AGENT_START_SOURCE\x10\x1b\x12\"\n\x1e\x43OLD_TRANSFER_AGENT_END_SOURCE\x10\x1c\x12)\n%COLD_TRANSFER_AGENT_START_DESTINATION\x10\x1d\x12\'\n#COLD_TRANSFER_AGENT_END_DESTINATION\x10\x1e\x12\x0e\n\nHOLD_START\x10\x1f\x12\x0c\n\x08HOLD_END\x10 \x12\x0b\n\x07REQUEUE\x10!\x12\x1c\n\x18\x43\x41LLER_SENT_TO_VOICEMAIL\x10\"\x12\x13\n\x0fRECORDING_START\x10#\x12\x12\n\x0eRECORDING_STOP\x10$\x12\x16\n\x12PBR_STARTED_RECORD\x10%\x12\x17\n\x13PBR_FINISHED_RECORD\x10&\x12\x0e\n\nACD_LOGOUT\x10\'\x12\x10\n\x0c\x41\x43\x44_REGISTER\x10(\x12\x1a\n\x16\x45XECUTED_AGENT_WEBLINK\x10)\x12\x18\n\x14TRANSFER_HOLD_CALLER\x10*\x12\x1a\n\x16TRANSFER_UNHOLD_CALLER\x10+\x12\x17\n\x13TRANSFER_HOLD_AGENT\x10,\x12\x19\n\x15TRANSFER_UNHOLD_AGENT\x10-\x12\x11\n\rTRANSFER_HOLD\x10.\x12\x13\n\x0fTRANSFER_UNHOLD\x10/\x12\x1a\n\x16TRANSFER_HOLD_OUTBOUND\x10\x30\x12\x1c\n\x18TRANSFER_UNHOLD_OUTBOUND\x10\x31\x12\x19\n\x15TRANSFER_ADD_OUTBOUND\x10\x32\x12\x1c\n\x18TRANSFER_REMOVE_OUTBOUND\x10\x33\x12\x1e\n\x1aWARM_CALLER_TRANSFER_START\x10\x34\x12.\n*WARM_CALLER_TRANSFER_INVITE_CALLER_INITIAL\x10\x35\x12&\n\"WARM_CALLER_TRANSFER_INVITE_CALLER\x10\x36\x12\x1c\n\x18WARM_CALLER_TRANSFER_END\x10\x37\x12\x12\n\x0e\x42\x41RGE_IN_START\x10\x38\x12\x11\n\rBARGE_IN_STOP\x10\x39\x12\x15\n\x11\x42\x61rgeInCallJoined\x10:\x12\x13\n\x0f\x42\x61rgeInCallLeft\x10;\"\xd2\n\n\x15\x41gentCallLogActionKey\"\xb8\n\n\x04\x45num\x12\x0c\n\x08\x44NCL_ADD\x10\x00\x12\x0e\n\nCALL_ENDED\x10\x01\x12\x13\n\x0f\x43\x41LL_DISCONNECT\x10\x02\x12\x11\n\rCALLER_HUNGUP\x10\x03\x12-\n)WARM_TRANSFER_AGENT_INVITE_CALLER_INITIAL\x10\x04\x12%\n!WARM_TRANSFER_AGENT_INVITE_CALLER\x10\x05\x12\x1d\n\x19WARM_TRANSFER_AGENT_START\x10\x06\x12\x1b\n\x17WARM_TRANSFER_AGENT_END\x10\x07\x12(\n$WARM_TRANSFER_OUTBOUND_INVITE_CALLER\x10\x08\x12\x30\n,WARM_TRANSFER_OUTBOUND_INVITE_CALLER_INITIAL\x10\t\x12 \n\x1cWARM_TRANSFER_OUTBOUND_START\x10\n\x12\x1e\n\x1aWARM_TRANSFER_OUTBOUND_END\x10\x0b\x12\x1d\n\x19\x43OLD_TRANSFER_AGENT_START\x10\x0c\x12\x1b\n\x17\x43OLD_TRANSFER_AGENT_END\x10\r\x12 \n\x1c\x43OLD_TRANSFER_OUTBOUND_START\x10\x0e\x12\x1a\n\x16\x43\x41LLBACK_SUSPEND_START\x10\x0f\x12\x15\n\x11\x43\x41LLBACK_RESUMING\x10\x10\x12\x11\n\rVOICEMAIL_END\x10\x11\x12\x1c\n\x18\x43\x41LLER_SENT_TO_VOICEMAIL\x10\x12\x12\x0e\n\nHOLD_START\x10\x13\x12\x0c\n\x08HOLD_END\x10\x14\x12\x13\n\x0fRECORDING_START\x10\x15\x12\x12\n\x0eRECORDING_STOP\x10\x16\x12\x15\n\x11\x43\x41LL_SKILLS_SCORE\x10\x17\x12\x17\n\x13\x43\x41LL_SKILLS_MATCHED\x10\x18\x12\x17\n\x13\x43\x41LL_SKILLS_CURRENT\x10\x19\x12\x17\n\x13\x43\x41LL_SKILLS_INITIAL\x10\x1a\x12\x1d\n\x19SKILLS_CHANGED_DROPSKILLS\x10\x1b\x12\x1c\n\x18SKILLS_CHANGED_ADDSKILLS\x10\x1c\x12\x0b\n\x07REQUEUE\x10\x1d\x12\x1a\n\x16SKILLS_CHANGED_REQUEUE\x10\x1e\x12\x12\n\x0eSCRUB_OVERRIDE\x10\x1f\x12,\n(CALLBACK_RESUMING_WITH_MANUAL_CALL_START\x10 \x12-\n)CALLBACK_RESUMING_WITH_MANUAL_CALL_FINISH\x10!\x12/\n+CALLBACK_RESUMING_WITH_MANUAL_CALL_TIMEDOUT\x10\"\x12/\n+CALLBACK_RESUMING_WITH_MANUAL_CALL_REPLACED\x10#\x12\x11\n\rTRANSFER_HOLD\x10$\x12\x13\n\x0fTRANSFER_UNHOLD\x10%\x12%\n!WARM_CALLER_TRANSFER_SOURCE_START\x10&\x12*\n&WARM_CALLER_TRANSFER_DESTINATION_START\x10\'\x12.\n*WARM_CALLER_TRANSFER_INVITE_CALLER_INITIAL\x10(\x12&\n\"WARM_CALLER_TRANSFER_INVITE_CALLER\x10)\x12\x1c\n\x18WARM_CALLER_TRANSFER_END\x10*\x12\x12\n\x0e\x42\x41RGE_IN_START\x10+\x12\x11\n\rBARGE_IN_STOP\x10,\"n\n\x17\x41gentCallLogActionValue\"S\n\x04\x45num\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x16\n\x12\x44NCL_RESULT_FAILED\x10\x01\x12\"\n\x1e\x43\x41LL_ENDED_CALLER_DISCONNECTED\x10\x02\"\xc1\x1b\n\x11HuntGroupParamKey\"\xab\x1b\n\x04\x45num\x12\x18\n\x14\x41GENT_DIAL_IN_NUMBER\x10\x00\x12\'\n#AGENT_LOGIN_GUI_STATISTICS_TEMPLATE\x10\x01\x12\"\n\x1e\x41GENT_PASSWORD_REQUIRES_LETTER\x10\x02\x12\"\n\x1e\x41GENT_PASSWORD_REQUIRES_NUMBER\x10\x03\x12\"\n\x1e\x41GENT_PASSWORD_REQUIRES_SYMBOL\x10\x04\x12\'\n#AGENT_PASSWORD_REQUIRES_UPPER_LOWER\x10\x05\x12\x1d\n\x19\x41GENT_SKILLS_REASSIGNMENT\x10\x06\x12\x1c\n\x18\x41GENT_STATS_CALL_HISTORY\x10\x07\x12\x11\n\rAGENT_TRIGGER\x10\x08\x12&\n\"AGENT_DISPOSITION_CONDITIONAL_DNCL\x10\t\x12\x0f\n\x0b\x41LLOWED_IPS\x10\n\x12\x14\n\x10\x41LLOW_AGENT_HOLD\x10\x0b\x12\x18\n\x14\x41LLOW_AGENT_INTERCOM\x10\x0c\x12\x1e\n\x1a\x41LLOW_AGENT_PASSWORD_RESET\x10\r\x12 \n\x1c\x41LLOW_AGENT_PAUSE_CODE_RESET\x10\x0e\x12\x18\n\x14\x41LLOW_AGENT_TO_PAUSE\x10\x0f\x12\x1d\n\x19\x41LLOW_CALLBACK_SCHEDULING\x10\x10\x12&\n\"ALLOW_EXPORT_PHONE_NUMBER_ACTIVITY\x10\x11\x12\"\n\x1e\x41LLOW_MANUAL_APPROVAL_OF_CALLS\x10\x12\x12\x18\n\x14\x41LLOW_MANUAL_DIALING\x10\x13\x12\x1f\n\x1b\x41LLOW_PHONE_NUMBER_ACTIVITY\x10\x14\x12\x1d\n\x19\x41LLOW_PREVIEW_DIAL_CANCEL\x10\x15\x12$\n ALLOW_SCHEDULED_CALLBACK_CALLING\x10\x16\x12\x18\n\x14\x41LLOW_TRANSFER_CALLS\x10\x17\x12\x17\n\x13\x41LPHANUMERIC_KEYPAD\x10\x18\x12\x1c\n\x18\x41UTO_PAUSE_ON_MULTI_HOLD\x10\x19\x12 \n\x1c\x41UTO_PAUSE_ON_PREVIEW_CANCEL\x10\x1a\x12\x1c\n\x18\x44\x45\x46\x41ULT_AGENT_PAUSE_CODE\x10\x1b\x12%\n!DEFAULT_AGENT_TRANSFERS_FILTERING\x10\x1c\x12\x18\n\x14\x44\x45\x46\x41ULT_DNCL_COUNTRY\x10\x1d\x12\x1b\n\x17\x44\x45\x46\x41ULT_DNCL_EXPIRATION\x10\x1e\x12(\n$DEFAULT_INBOUND_CALL_DNCL_EXPIRATION\x10\x1f\x12\'\n#DEFAULT_MANUAL_CALL_DNCL_EXPIRATION\x10 \x12)\n%DEFAULT_OUTBOUND_CALL_DNCL_EXPIRATION\x10!\x12(\n$DEFAULT_PREVIEW_CALL_DNCL_EXPIRATION\x10\"\x12&\n\"DEFAULT_SCHEDULED_CALLBACK_ROUTING\x10#\x12 \n\x1c\x44ISCONNECT_CALL_CONFIRMATION\x10$\x12%\n!DISPLAY_AGENT_TRANSFERS_FILTERING\x10%\x12\x1d\n\x19\x44ISPLAY_DATA_COLLECT_DATA\x10&\x12\x1c\n\x18\x44ISPLAY_DATA_DIPPED_DATA\x10\'\x12\x1c\n\x18\x44ISPLAY_IVR_KEYS_PRESSED\x10(\x12\x1e\n\x1a\x44ISPLAY_PHONE_ZIP_METADATA\x10)\x12\x1f\n\x1b\x44ISPLAY_RECORDING_INDICATOR\x10*\x12\x15\n\x11\x44O_ALLOW_ADD_DNCL\x10+\x12\x1a\n\x16\x45NABLE_RECORDING_PAUSE\x10,\x12\x19\n\x15HOLD_QUEUE_MONITORING\x10-\x12\'\n#HOLD_QUEUE_MONITORING_AGENT_ROUTING\x10.\x12\x36\n2HOLD_QUEUE_MONITORING_PREFERRED_HUNT_GROUP_ROUTING\x10/\x12\x35\n1HOLD_QUEUE_MONITORING_REQUIRED_HUNT_GROUP_ROUTING\x10\x30\x12+\n\'HUNT_GROUP_CLIENT_INFO_DISPLAY_TEMPLATE\x10\x31\x12\x15\n\x11HUNT_GROUP_SCRIPT\x10\x32\x12\x17\n\x13HUNT_GROUP_WEB_LINK\x10\x33\x12\'\n#MANUAL_APPROVAL_NUMBER_CONFIRMATION\x10\x34\x12\x1d\n\x19MANUAL_DIAL_AUTO_DNCL_ADD\x10\x35\x12!\n\x1dMANUAL_DIAL_DEFAULT_CALLER_ID\x10\x36\x12\x1f\n\x1bMANUAL_DIAL_DEFAULT_COUNTRY\x10\x37\x12+\n\'MANUAL_DIAL_DISPLAY_COUNTRY_SELECT_MENU\x10\x38\x12)\n%MANUAL_DIAL_DEFAULT_CALLER_ID_COUNTRY\x10\x39\x12\x35\n1MANUAL_DIAL_DISPLAY_CALLER_ID_COUNTRY_SELECT_MENU\x10:\x12\x32\n.MANUAL_DIAL_DISPLAY_OUTBOUND_NUMBER_PHONE_BOOK\x10;\x12\"\n\x1eMANUAL_DIAL_DISPLAY_PHONE_BOOK\x10<\x12!\n\x1dMANUAL_DIAL_NUMBER_WHITE_LIST\x10=\x12#\n\x1fMANUAL_DIAL_OVERRIDE_CELL_SCRUB\x10>\x12+\n\'MANUAL_DIAL_OVERRIDE_RECORDING_SETTINGS\x10@\x12\x1e\n\x1aMANUAL_DIAL_SCRUB_OVERRIDE\x10\x41\x12!\n\x1dMANUAL_DIAL_TIMEZONE_OVERRIDE\x10\x42\x12\'\n#MANUAL_DIAL_USER_EDITABLE_CALLER_ID\x10\x43\x12#\n\x1fMANUAL_QUEUE_CONFIGURATION_NAME\x10\x44\x12!\n\x1dMINIMUM_AGENT_PASSWORD_LENGTH\x10\x45\x12(\n$PHONE_NUMBER_ACTIVITY_EDIT_RESPONSES\x10\x46\x12-\n)PHONE_NUMBER_ACTIVITY_RECORDINGS_DOWNLOAD\x10G\x12\x1e\n\x1aPREVIEW_DIAL_AUTO_DNCL_ADD\x10H\x12\x1d\n\x19PREVIEW_DIAL_CALL_TIMEOUT\x10I\x12\x1d\n\x19PREVIEW_DIAL_CONFIRMATION\x10J\x12$\n PREVIEW_QUEUE_CONFIGURATION_NAME\x10K\x12\x13\n\x0fRECORDING_DELAY\x10L\x12-\n)REQUEUE_TRANSFER_QUEUE_CONFIGURATION_NAME\x10M\x12&\n\"SCHEDULED_CALLBACKS_RETRIEVAL_MODE\x10N\x12)\n%SCHEDULED_CALLBACK_ROUTING_DISALLOWED\x10O\x12$\n TRANSFER_CALLS_DEFAULT_CALLER_ID\x10P\x12\"\n\x1eTRANSFER_CALLS_DEFAULT_COUNTRY\x10Q\x12*\n&TRANSFER_CALLS_DEFAULT_TRANSFER_NUMBER\x10R\x12/\n+TRANSFER_CALLS_DISPLAY_CALLER_ID_PHONE_BOOK\x10S\x12.\n*TRANSFER_CALLS_DISPLAY_COUNTRY_SELECT_MENU\x10T\x12\x35\n1TRANSFER_CALLS_DISPLAY_TRANSFER_NUMBER_PHONE_BOOK\x10U\x12 \n\x1cTRANSFER_CALLS_HAND_OFF_TYPE\x10V\x12 \n\x1cTRANSFER_CALLS_TRANSFER_TYPE\x10W\x12*\n&TRANSFER_CALLS_USER_EDITABLE_CALLER_ID\x10X\x12\x30\n,TRANSFER_CALLS_USER_EDITABLE_TRANSFER_NUMBER\x10Y\x12\x1d\n\x19TRANSFER_RECORDING_STATUS\x10Z\x12\x1e\n\x1aUSE_ADVANCED_GATEWAY_TITLE\x10[\x12\x19\n\x15USE_AGENT_PAUSE_CODES\x10\\\x12\x15\n\x11USE_IP_BASED_AUTH\x10]\x12&\n\"HUNT_GROUP_REASSIGNMENT_DISALLOWED\x10^\x12&\n\"REQUEUE_TRANSFER_DISALLOWED_SKILLS\x10_\x12\'\n#ALLOW_MANUAL_APPROVAL_FOR_MESSAGING\x10`\x12\x12\n\x0e\x44ISPLAY_SKILLS\x10\x61\x12&\n\"PBX_TRANSFER_DISALLOWED_EXTENSIONS\x10\x62\"?\n\rReplaceConfig\".\n\x04\x45num\x12\r\n\tNO_CHANGE\x10\x00\x12\n\n\x06TENANT\x10\x01\x12\x0b\n\x07REPLACE\x10\x02\"\xc7\x02\n\x0eTransferMember\x12\x1e\n\nidentifier\x18\x01 \x01(\tR\nidentifier\x12#\n\rdisplay_label\x18\x02 \x01(\tR\x0c\x64isplayLabel\x12@\n\x0bmember_type\x18\x03 \x01(\x0e\x32\x1f.api.commons.TransferMemberTypeR\nmemberType\x12@\n\ragent_session\x18\x64 \x01(\x0b\x32\x19.api.commons.AgentSessionH\x00R\x0c\x61gentSession\x12\x37\n\ncaller_sid\x18\x65 \x01(\x0b\x32\x16.api.commons.CallerSidH\x00R\tcallerSid\x12!\n\x0boutbound_id\x18\x66 \x01(\tH\x00R\noutboundIdB\x10\n\x0elocatable_data\"\xb1\x02\n\nAgentAlert\x12Y\n\x12\x62\x61\x63koffice_message\x18\x01 \x01(\x0b\x32(.api.commons.AgentBackofficeMessageAlertH\x00R\x11\x62\x61\x63kofficeMessage\x12`\n\x15\x64irected_call_ringing\x18\x02 \x01(\x0b\x32*.api.commons.AgentDirectedCallRingingAlertH\x00R\x13\x64irectedCallRinging\x12]\n\x14\x64irected_call_hangup\x18\x03 \x01(\x0b\x32).api.commons.AgentDirectedCallHangupAlertH\x00R\x12\x64irectedCallHangupB\x07\n\x05\x61lert\"\xf7\x01\n\x1b\x41gentBackofficeMessageAlert\x12\'\n\x0f\x65xpire_duration\x18\x01 \x01(\x03R\x0e\x65xpireDuration\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12K\n\x14target_agent_session\x18\x03 \x01(\x0b\x32\x19.api.commons.AgentSessionR\x12targetAgentSession\x12\x18\n\x07message\x18\x04 \x01(\tR\x07message\x12\x0e\n\x02id\x18\x05 \x01(\tR\x02id\"\xe2\x02\n\x1d\x41gentDirectedCallRingingAlert\x12\'\n\x0f\x65xpire_duration\x18\x01 \x01(\x03R\x0e\x65xpireDuration\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12K\n\x14target_agent_session\x18\x03 \x01(\x0b\x32\x19.api.commons.AgentSessionR\x12targetAgentSession\x12\x35\n\ncaller_sid\x18\x04 \x01(\x0b\x32\x16.api.commons.CallerSidR\tcallerSid\x12\x1b\n\tcaller_id\x18\x05 \x01(\tR\x08\x63\x61llerId\x12-\n\x12\x64\x65stination_number\x18\x06 \x01(\tR\x11\x64\x65stinationNumber\x12\x0e\n\x02id\x18\x07 \x01(\tR\x02id\"\x95\x02\n\x1c\x41gentDirectedCallHangupAlert\x12\'\n\x0f\x65xpire_duration\x18\x01 \x01(\x03R\x0e\x65xpireDuration\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12K\n\x14target_agent_session\x18\x03 \x01(\x0b\x32\x19.api.commons.AgentSessionR\x12targetAgentSession\x12\x35\n\ncaller_sid\x18\x04 \x01(\x0b\x32\x16.api.commons.CallerSidR\tcallerSid\x12\x0e\n\x02id\x18\x05 \x01(\tR\x02id\"\xe4\x05\n\nAgentState\x12\x16\n\x06status\x18\x02 \x01(\x03R\x06status\x12>\n\x0bstatus_desc\x18\x03 \x01(\x0e\x32\x1d.api.commons.AgentStatus.EnumR\nstatusDesc\x12\x16\n\x06paused\x18\x04 \x01(\x08R\x06paused\x12\x14\n\x05queue\x18\x05 \x01(\tR\x05queue\x12,\n\x12\x63urrent_session_id\x18\x06 \x01(\x03R\x10\x63urrentSessionId\x12,\n\x12last_status_change\x18\x07 \x01(\x03R\x10lastStatusChange\x12\x1e\n\nmonitoring\x18\x08 \x01(\x08R\nmonitoring\x12\x1f\n\x0b\x63\x61lls_count\x18\t \x01(\x03R\ncallsCount\x12\"\n\rlast_sip_code\x18\n \x01(\x03R\x0blastSipCode\x12\x34\n\x17\x61gent_peer_is_lost_call\x18\x0b \x01(\x08R\x13\x61gentPeerIsLostCall\x12\x1a\n\x08\x64isabled\x18\x0c \x01(\x08R\x08\x64isabled\x12\x30\n\x14\x63\x61ller_was_suspended\x18\r \x01(\x08R\x12\x63\x61llerWasSuspended\x12\x46\n\x10transfer_members\x18\x0e \x03(\x0b\x32\x1b.api.commons.TransferMemberR\x0ftransferMembers\x12?\n\x1d\x61gent_peer_is_direct_to_agent\x18\x0f \x01(\x08R\x18\x61gentPeerIsDirectToAgent\x12\x17\n\x07user_id\x18\x10 \x01(\tR\x06userId\x12\x1b\n\tagent_sid\x18\x11 \x01(\x03R\x08\x61gentSid\x12&\n\x0f\x61sm_session_sid\x18\x12 \x01(\x03R\rasmSessionSid\x12$\n\x0e\x61gent_is_muted\x18\x13 \x01(\x08R\x0c\x61gentIsMuted*\xb7\x01\n\tACDStatus\x12\x0f\n\x0b\x41\x43\x44_UNKNOWN\x10\x00\x12\x1d\n\x18\x41GENT_SESSION_LOGGING_IN\x10\x84 \x12\x1c\n\x17\x41GENT_SESSION_LOGGED_IN\x10\x8e \x12\x1c\n\x17\x41GENT_SESSION_COMPLETED\x10\xe8 \x12\x19\n\x14\x41GENT_SESSION_SUMMED\x10\xcc!\x12#\n\x1e\x41GENT_SESSION_ACCOUNTINGEXPORT\x10\xb0\"*\xa4\x01\n\x15\x41gentCallLogCallEnded\x12\x13\n\x0f\x41GENT_CANCELLED\x10\x00\x12\x17\n\x13\x43\x41LLER_DISCONNECTED\x10\x01\x12\x11\n\rNOT_CONNECTED\x10\x02\x12\x0e\n\nAGENT_LOST\x10\x03\x12\x10\n\x0c\x41GENT_HANGUP\x10\x04\x12\x11\n\rCALLER_HANGUP\x10\x05\x12\x15\n\x11\x43\x41LL_END_ESTIMATE\x10\x06*.\n\x08HoldType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06SIMPLE\x10\x01\x12\t\n\x05MULTI\x10\x02*\xfa\x01\n\x16QueuedNotificationType\x12*\n&QueuedNotificationType_GENERAL_INITIAL\x10\x00\x12&\n\"QueuedNotificationType_PBX_INITIAL\x10\x01\x12.\n*QueuedNotificationType_AGENT_BOUND_INITIAL\x10\x02\x12+\n\'QueuedNotificationType_GENERAL_REQUEUED\x10\x03\x12/\n+QueuedNotificationType_AGENT_BOUND_REQUEUED\x10\x04*r\n\x12TransferMemberType\x12\x1c\n\x18TransferMemberType_AGENT\x10\x00\x12\x1d\n\x19TransferMemberType_CALLER\x10\x01\x12\x1f\n\x1bTransferMemberType_OUTBOUND\x10\x02*\xa2\x02\n\tDTMFDigit\x12\x0f\n\x0b\x44TMFDigit_0\x10\x00\x12\x0f\n\x0b\x44TMFDigit_1\x10\x01\x12\x0f\n\x0b\x44TMFDigit_2\x10\x02\x12\x0f\n\x0b\x44TMFDigit_3\x10\x03\x12\x0f\n\x0b\x44TMFDigit_4\x10\x04\x12\x0f\n\x0b\x44TMFDigit_5\x10\x05\x12\x0f\n\x0b\x44TMFDigit_6\x10\x06\x12\x0f\n\x0b\x44TMFDigit_7\x10\x07\x12\x0f\n\x0b\x44TMFDigit_8\x10\x08\x12\x0f\n\x0b\x44TMFDigit_9\x10\t\x12\x0f\n\x0b\x44TMFDigit_A\x10\n\x12\x0f\n\x0b\x44TMFDigit_B\x10\x0b\x12\x0f\n\x0b\x44TMFDigit_C\x10\x0c\x12\x0f\n\x0b\x44TMFDigit_D\x10\r\x12\x12\n\x0e\x44TMFDigit_STAR\x10\x0e\x12\x13\n\x0f\x44TMFDigit_POUND\x10\x0f\x42h\n\x0f\x63om.api.commonsB\x08\x41\x63\x64ProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.acd_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\010AcdProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_ACDSTATUS']._serialized_start=11259
  _globals['_ACDSTATUS']._serialized_end=11442
  _globals['_AGENTCALLLOGCALLENDED']._serialized_start=11445
  _globals['_AGENTCALLLOGCALLENDED']._serialized_end=11609
  _globals['_HOLDTYPE']._serialized_start=11611
  _globals['_HOLDTYPE']._serialized_end=11657
  _globals['_QUEUEDNOTIFICATIONTYPE']._serialized_start=11660
  _globals['_QUEUEDNOTIFICATIONTYPE']._serialized_end=11910
  _globals['_TRANSFERMEMBERTYPE']._serialized_start=11912
  _globals['_TRANSFERMEMBERTYPE']._serialized_end=12026
  _globals['_DTMFDIGIT']._serialized_start=12029
  _globals['_DTMFDIGIT']._serialized_end=12319
  _globals['_AGENTSESSION']._serialized_start=72
  _globals['_AGENTSESSION']._serialized_end=296
  _globals['_CALLERSID']._serialized_start=299
  _globals['_CALLERSID']._serialized_end=443
  _globals['_AGENTSTATUS']._serialized_start=446
  _globals['_AGENTSTATUS']._serialized_end=1535
  _globals['_AGENTSTATUS_ENUM']._serialized_start=462
  _globals['_AGENTSTATUS_ENUM']._serialized_end=1535
  _globals['_CALLERSTATUS']._serialized_start=1538
  _globals['_CALLERSTATUS']._serialized_end=2011
  _globals['_CALLERSTATUS_ENUM']._serialized_start=1555
  _globals['_CALLERSTATUS_ENUM']._serialized_end=2011
  _globals['_CALLTYPE']._serialized_start=2013
  _globals['_CALLTYPE']._serialized_end=2092
  _globals['_CALLTYPE_ENUM']._serialized_start=2025
  _globals['_CALLTYPE_ENUM']._serialized_end=2092
  _globals['_AGENTDIALIN']._serialized_start=2094
  _globals['_AGENTDIALIN']._serialized_end=2156
  _globals['_AGENTDIALIN_ENUM']._serialized_start=2109
  _globals['_AGENTDIALIN_ENUM']._serialized_end=2156
  _globals['_HUNTGROUPTYPE']._serialized_start=2158
  _globals['_HUNTGROUPTYPE']._serialized_end=2228
  _globals['_HUNTGROUPTYPE_ENUM']._serialized_start=2175
  _globals['_HUNTGROUPTYPE_ENUM']._serialized_end=2228
  _globals['_AGENTSESSIONLOGACTIONKEY']._serialized_start=2231
  _globals['_AGENTSESSIONLOGACTIONKEY']._serialized_end=3922
  _globals['_AGENTSESSIONLOGACTIONKEY_ENUM']._serialized_start=2260
  _globals['_AGENTSESSIONLOGACTIONKEY_ENUM']._serialized_end=3922
  _globals['_AGENTCALLLOGACTIONKEY']._serialized_start=3925
  _globals['_AGENTCALLLOGACTIONKEY']._serialized_end=5287
  _globals['_AGENTCALLLOGACTIONKEY_ENUM']._serialized_start=3951
  _globals['_AGENTCALLLOGACTIONKEY_ENUM']._serialized_end=5287
  _globals['_AGENTCALLLOGACTIONVALUE']._serialized_start=5289
  _globals['_AGENTCALLLOGACTIONVALUE']._serialized_end=5399
  _globals['_AGENTCALLLOGACTIONVALUE_ENUM']._serialized_start=5316
  _globals['_AGENTCALLLOGACTIONVALUE_ENUM']._serialized_end=5399
  _globals['_HUNTGROUPPARAMKEY']._serialized_start=5402
  _globals['_HUNTGROUPPARAMKEY']._serialized_end=8923
  _globals['_HUNTGROUPPARAMKEY_ENUM']._serialized_start=5424
  _globals['_HUNTGROUPPARAMKEY_ENUM']._serialized_end=8923
  _globals['_REPLACECONFIG']._serialized_start=8925
  _globals['_REPLACECONFIG']._serialized_end=8988
  _globals['_REPLACECONFIG_ENUM']._serialized_start=8942
  _globals['_REPLACECONFIG_ENUM']._serialized_end=8988
  _globals['_TRANSFERMEMBER']._serialized_start=8991
  _globals['_TRANSFERMEMBER']._serialized_end=9318
  _globals['_AGENTALERT']._serialized_start=9321
  _globals['_AGENTALERT']._serialized_end=9626
  _globals['_AGENTBACKOFFICEMESSAGEALERT']._serialized_start=9629
  _globals['_AGENTBACKOFFICEMESSAGEALERT']._serialized_end=9876
  _globals['_AGENTDIRECTEDCALLRINGINGALERT']._serialized_start=9879
  _globals['_AGENTDIRECTEDCALLRINGINGALERT']._serialized_end=10233
  _globals['_AGENTDIRECTEDCALLHANGUPALERT']._serialized_start=10236
  _globals['_AGENTDIRECTEDCALLHANGUPALERT']._serialized_end=10513
  _globals['_AGENTSTATE']._serialized_start=10516
  _globals['_AGENTSTATE']._serialized_end=11256
# @@protoc_insertion_point(module_scope)
