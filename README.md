# ESM API Docs crawler
Crawl the ESM API docs and extract all resources. 

Install 
```
python3 -m pip install git+https://github.com/mfesiem/esm_api_docs_crawler.git
```

CLI Usage:

```
% python3 -m esm_api_docs_crawler -h                               
usage: python3 -m esm_api_docs_crawler [-h] --url URL

Crawl the ESM API docs and print all URLs

optional arguments:
  -h, --help  show this help message and exit
  --url URL   SIEM API help URL. (default: None)
```

Python usage:
```python
from esm_api_docs_crawler import get_ressources

summary, methods, types = get_ressources('https://ESM_URL/rs/esm/v2/help')

print(summary['url'] + '\n' + summary['html'])
[ print(m['url']) for m in methods ]
[ print(t['url']) for t in types ]
```


CLI Exemple:
```
% python3 -m esm_api_docs_crawler --url https://ESM_URL/rs/esm/v2/help 
Crawling SIEM API ressources docs...
https://ESM_URL/rs/esm/v2/help
https://ESM_URL/rs/esm/v2/help/alarmAcknowledgeTriggeredAlarm
https://ESM_URL/rs/esm/v2/help/alarmDeleteTriggeredAlarm
https://ESM_URL/rs/esm/v2/help/alarmGetTriggeredAlarms
https://ESM_URL/rs/esm/v2/help/alarmUnacknowledgeTriggeredAlarm
https://ESM_URL/rs/esm/v2/help/assetGetAssetDetailsObject
https://ESM_URL/rs/esm/v2/help/assetGetAssetThreats
https://ESM_URL/rs/esm/v2/help/caseAddCase
https://ESM_URL/rs/esm/v2/help/caseAddCaseStatus
https://ESM_URL/rs/esm/v2/help/caseAddOrganization
https://ESM_URL/rs/esm/v2/help/caseDeleteCaseStatus
https://ESM_URL/rs/esm/v2/help/caseEditCase
https://ESM_URL/rs/esm/v2/help/caseEditCaseStatus
https://ESM_URL/rs/esm/v2/help/caseEditOrganization
https://ESM_URL/rs/esm/v2/help/caseGetCaseDetail
https://ESM_URL/rs/esm/v2/help/caseGetCaseEventsDetail
https://ESM_URL/rs/esm/v2/help/caseGetCaseList
https://ESM_URL/rs/esm/v2/help/caseGetCaseStatusList
https://ESM_URL/rs/esm/v2/help/caseGetCaseUsers
https://ESM_URL/rs/esm/v2/help/caseGetOrganizationList
https://ESM_URL/rs/esm/v2/help/devGetDeviceList
https://ESM_URL/rs/esm/v2/help/dsAddDataSourceClients
https://ESM_URL/rs/esm/v2/help/dsAddDataSourceClientsStatus
https://ESM_URL/rs/esm/v2/help/dsAddDataSources
https://ESM_URL/rs/esm/v2/help/dsAddDataSourcesStatus
https://ESM_URL/rs/esm/v2/help/dsDeleteDataSourceClients
https://ESM_URL/rs/esm/v2/help/dsDeleteDataSources
https://ESM_URL/rs/esm/v2/help/dsEditDataSource
https://ESM_URL/rs/esm/v2/help/dsEditDataSourceClient
https://ESM_URL/rs/esm/v2/help/dsGetDataSourceClients
https://ESM_URL/rs/esm/v2/help/dsGetDataSourceDetail
https://ESM_URL/rs/esm/v2/help/dsGetDataSourceList
https://ESM_URL/rs/esm/v2/help/dsGetDataSourceTypes
https://ESM_URL/rs/esm/v2/help/dsGetEpoList
https://ESM_URL/rs/esm/v2/help/dsGetUserDefinedDataSources
https://ESM_URL/rs/esm/v2/help/dsSetUserDefinedDataSources
https://ESM_URL/rs/esm/v2/help/dsWriteThirdpartyConfig
https://ESM_URL/rs/esm/v2/help/essmgtGetBuildStamp
https://ESM_URL/rs/esm/v2/help/essmgtGetESSTime
https://ESM_URL/rs/esm/v2/help/geoGetGeoLocRegionList
https://ESM_URL/rs/esm/v2/help/geoGetGeoLocs
https://ESM_URL/rs/esm/v2/help/getActiveResponseCollectors
https://ESM_URL/rs/esm/v2/help/grpGetDeviceTree
https://ESM_URL/rs/esm/v2/help/grpGetDeviceTreeEx
https://ESM_URL/rs/esm/v2/help/ipsGetAlertData
https://ESM_URL/rs/esm/v2/help/ipsGetCorrRawEvents
https://ESM_URL/rs/esm/v2/help/miscJobStatus
https://ESM_URL/rs/esm/v2/help/miscKeepAlive
https://ESM_URL/rs/esm/v2/help/notifyGetTriggeredNotificationDetail
https://ESM_URL/rs/esm/v2/help/plcyGetPolicyList
https://ESM_URL/rs/esm/v2/help/plcyGetVariableList
https://ESM_URL/rs/esm/v2/help/plcyRollPolicy
https://ESM_URL/rs/esm/v2/help/qryClose
https://ESM_URL/rs/esm/v2/help/qryExecute
https://ESM_URL/rs/esm/v2/help/qryExecuteDetail
https://ESM_URL/rs/esm/v2/help/qryExecuteGrouped
https://ESM_URL/rs/esm/v2/help/qryGetCorrEventDataForID
https://ESM_URL/rs/esm/v2/help/qryGetFilterFields
https://ESM_URL/rs/esm/v2/help/qryGetResults
https://ESM_URL/rs/esm/v2/help/qryGetSelectFields
https://ESM_URL/rs/esm/v2/help/qryGetStatus
https://ESM_URL/rs/esm/v2/help/runActiveResponseSearch
https://ESM_URL/rs/esm/v2/help/sysAddWatchlist
https://ESM_URL/rs/esm/v2/help/sysAddWatchlistValues
https://ESM_URL/rs/esm/v2/help/sysEditWatchlist
https://ESM_URL/rs/esm/v2/help/sysGetWatchlistDetails
https://ESM_URL/rs/esm/v2/help/sysGetWatchlistFields
https://ESM_URL/rs/esm/v2/help/sysGetWatchlistValues
https://ESM_URL/rs/esm/v2/help/sysGetWatchlists
https://ESM_URL/rs/esm/v2/help/sysRemoveWatchlist
https://ESM_URL/rs/esm/v2/help/sysRemoveWatchlistValues
https://ESM_URL/rs/esm/v2/help/userAddAccessGroup
https://ESM_URL/rs/esm/v2/help/userAddUser
https://ESM_URL/rs/esm/v2/help/userCaseList
https://ESM_URL/rs/esm/v2/help/userDeleteAccessGroup
https://ESM_URL/rs/esm/v2/help/userDeleteUser
https://ESM_URL/rs/esm/v2/help/userEditAccessGroup
https://ESM_URL/rs/esm/v2/help/userEditUser
https://ESM_URL/rs/esm/v2/help/userGetAccessGroupDetail
https://ESM_URL/rs/esm/v2/help/userGetAccessGroupList
https://ESM_URL/rs/esm/v2/help/userGetRightsList
https://ESM_URL/rs/esm/v2/help/userGetTimeZones
https://ESM_URL/rs/esm/v2/help/userGetUserList
https://ESM_URL/rs/esm/v2/help/userGetUserRights
https://ESM_URL/rs/esm/v2/help/zoneAddSubZone
https://ESM_URL/rs/esm/v2/help/zoneAddZone
https://ESM_URL/rs/esm/v2/help/zoneDeleteSubZone
https://ESM_URL/rs/esm/v2/help/zoneDeleteZone
https://ESM_URL/rs/esm/v2/help/zoneEditSubZone
https://ESM_URL/rs/esm/v2/help/zoneEditZone
https://ESM_URL/rs/esm/v2/help/zoneGetSubZone
https://ESM_URL/rs/esm/v2/help/zoneGetZone
https://ESM_URL/rs/esm/v2/help/zoneGetZoneTree
https://ESM_URL/rs/esm/v2/help/types/AddDatasourceClientResponse
https://ESM_URL/rs/esm/v2/help/types/AddDatasourceResponse
https://ESM_URL/rs/esm/v2/help/types/AssetDetailsObject
https://ESM_URL/rs/esm/v2/help/types/AssetGroup
https://ESM_URL/rs/esm/v2/help/types/AssetId
https://ESM_URL/rs/esm/v2/help/types/DataSourceClientAdd
https://ESM_URL/rs/esm/v2/help/types/DataSourceData
https://ESM_URL/rs/esm/v2/help/types/DataSourceDataAdd
https://ESM_URL/rs/esm/v2/help/types/DatasourceDataEdit
https://ESM_URL/rs/esm/v2/help/types/EPOList
https://ESM_URL/rs/esm/v2/help/types/EPOListRequest
https://ESM_URL/rs/esm/v2/help/types/EPOServer
https://ESM_URL/rs/esm/v2/help/types/EsmAccessGroup
https://ESM_URL/rs/esm/v2/help/types/EsmAccessGroupDetail
https://ESM_URL/rs/esm/v2/help/types/EsmAccessGroupId
https://ESM_URL/rs/esm/v2/help/types/EsmAlarmId
https://ESM_URL/rs/esm/v2/help/types/EsmAlarmIds
https://ESM_URL/rs/esm/v2/help/types/EsmAlertData
https://ESM_URL/rs/esm/v2/help/types/EsmAlertId
https://ESM_URL/rs/esm/v2/help/types/EsmBasicValue
https://ESM_URL/rs/esm/v2/help/types/EsmBoolean
https://ESM_URL/rs/esm/v2/help/types/EsmBuildStamp
https://ESM_URL/rs/esm/v2/help/types/EsmCase
https://ESM_URL/rs/esm/v2/help/types/EsmCaseDetail
https://ESM_URL/rs/esm/v2/help/types/EsmCaseDetailExternal
https://ESM_URL/rs/esm/v2/help/types/EsmCaseEvent
https://ESM_URL/rs/esm/v2/help/types/EsmCaseId
https://ESM_URL/rs/esm/v2/help/types/EsmCaseOrganization
https://ESM_URL/rs/esm/v2/help/types/EsmCaseStatus
https://ESM_URL/rs/esm/v2/help/types/EsmCaseStatusId
https://ESM_URL/rs/esm/v2/help/types/EsmCaseUser
https://ESM_URL/rs/esm/v2/help/types/EsmCaseUserList
https://ESM_URL/rs/esm/v2/help/types/EsmCidr
https://ESM_URL/rs/esm/v2/help/types/EsmCompoundValue
https://ESM_URL/rs/esm/v2/help/types/EsmCustomType
https://ESM_URL/rs/esm/v2/help/types/EsmDataSource
https://ESM_URL/rs/esm/v2/help/types/EsmDataSourceClient
https://ESM_URL/rs/esm/v2/help/types/EsmDataSourceId
https://ESM_URL/rs/esm/v2/help/types/EsmDataSourceModel
https://ESM_URL/rs/esm/v2/help/types/EsmDataSourceParameter
https://ESM_URL/rs/esm/v2/help/types/EsmDataSourceType
https://ESM_URL/rs/esm/v2/help/types/EsmDataSourceTypeId
https://ESM_URL/rs/esm/v2/help/types/EsmDataSourceVendor
https://ESM_URL/rs/esm/v2/help/types/EsmDevice
https://ESM_URL/rs/esm/v2/help/types/EsmDeviceId
https://ESM_URL/rs/esm/v2/help/types/EsmDeviceTreeEx
https://ESM_URL/rs/esm/v2/help/types/EsmDeviceType
https://ESM_URL/rs/esm/v2/help/types/EsmEmailId
https://ESM_URL/rs/esm/v2/help/types/EsmEventId
https://ESM_URL/rs/esm/v2/help/types/EsmField
https://ESM_URL/rs/esm/v2/help/types/EsmFieldFilter
https://ESM_URL/rs/esm/v2/help/types/EsmFieldType
https://ESM_URL/rs/esm/v2/help/types/EsmFileData
https://ESM_URL/rs/esm/v2/help/types/EsmFileToken
https://ESM_URL/rs/esm/v2/help/types/EsmFilter
https://ESM_URL/rs/esm/v2/help/types/EsmFilterField
https://ESM_URL/rs/esm/v2/help/types/EsmFilterGroup
https://ESM_URL/rs/esm/v2/help/types/EsmFilterGroupLogic
https://ESM_URL/rs/esm/v2/help/types/EsmFilterOperator
https://ESM_URL/rs/esm/v2/help/types/EsmFilterValue
https://ESM_URL/rs/esm/v2/help/types/EsmGeoLoc
https://ESM_URL/rs/esm/v2/help/types/EsmGeoLocId
https://ESM_URL/rs/esm/v2/help/types/EsmGroupID
https://ESM_URL/rs/esm/v2/help/types/EsmGroupedQueryConfig
https://ESM_URL/rs/esm/v2/help/types/EsmGroupedQueryType
https://ESM_URL/rs/esm/v2/help/types/EsmJobId
https://ESM_URL/rs/esm/v2/help/types/EsmJobStatus
https://ESM_URL/rs/esm/v2/help/types/EsmNetworkAddress
https://ESM_URL/rs/esm/v2/help/types/EsmOrganizationId
https://ESM_URL/rs/esm/v2/help/types/EsmPassword
https://ESM_URL/rs/esm/v2/help/types/EsmPolicy
https://ESM_URL/rs/esm/v2/help/types/EsmPolicyId
https://ESM_URL/rs/esm/v2/help/types/EsmPolicyType
https://ESM_URL/rs/esm/v2/help/types/EsmPrivileges
https://ESM_URL/rs/esm/v2/help/types/EsmQueryColumn
https://ESM_URL/rs/esm/v2/help/types/EsmQueryColumnInfo
https://ESM_URL/rs/esm/v2/help/types/EsmQueryConfig
https://ESM_URL/rs/esm/v2/help/types/EsmQueryGroupType
https://ESM_URL/rs/esm/v2/help/types/EsmQueryId
https://ESM_URL/rs/esm/v2/help/types/EsmQueryResultID
https://ESM_URL/rs/esm/v2/help/types/EsmQueryResults
https://ESM_URL/rs/esm/v2/help/types/EsmQueryRow
https://ESM_URL/rs/esm/v2/help/types/EsmQueryStatus
https://ESM_URL/rs/esm/v2/help/types/EsmQueryType
https://ESM_URL/rs/esm/v2/help/types/EsmRestCalendar
https://ESM_URL/rs/esm/v2/help/types/EsmRight
https://ESM_URL/rs/esm/v2/help/types/EsmRightId
https://ESM_URL/rs/esm/v2/help/types/EsmRowOrder
https://ESM_URL/rs/esm/v2/help/types/EsmRunningQuery
https://ESM_URL/rs/esm/v2/help/types/EsmSelectField
https://ESM_URL/rs/esm/v2/help/types/EsmSmsId
https://ESM_URL/rs/esm/v2/help/types/EsmSortDirection
https://ESM_URL/rs/esm/v2/help/types/EsmSourceEvent
https://ESM_URL/rs/esm/v2/help/types/EsmSourceEvents
https://ESM_URL/rs/esm/v2/help/types/EsmSourceFlow
https://ESM_URL/rs/esm/v2/help/types/EsmStringList
https://ESM_URL/rs/esm/v2/help/types/EsmSubZone
https://ESM_URL/rs/esm/v2/help/types/EsmSubZoneId
https://ESM_URL/rs/esm/v2/help/types/EsmSubZoneInfo
https://ESM_URL/rs/esm/v2/help/types/EsmTimeRange
https://ESM_URL/rs/esm/v2/help/types/EsmTimeZone
https://ESM_URL/rs/esm/v2/help/types/EsmTimeZoneId
https://ESM_URL/rs/esm/v2/help/types/EsmTreeNode
https://ESM_URL/rs/esm/v2/help/types/EsmTreeNodeEx
https://ESM_URL/rs/esm/v2/help/types/EsmTriggeredAlarm
https://ESM_URL/rs/esm/v2/help/types/EsmTriggeredAlarmDetail
https://ESM_URL/rs/esm/v2/help/types/EsmTriggeredAlarmEvent
https://ESM_URL/rs/esm/v2/help/types/EsmUpdateType
https://ESM_URL/rs/esm/v2/help/types/EsmUser
https://ESM_URL/rs/esm/v2/help/types/EsmUserDefinedDataSource
https://ESM_URL/rs/esm/v2/help/types/EsmUserId
https://ESM_URL/rs/esm/v2/help/types/EsmUserRights
https://ESM_URL/rs/esm/v2/help/types/EsmUserType
https://ESM_URL/rs/esm/v2/help/types/EsmVariable
https://ESM_URL/rs/esm/v2/help/types/EsmVariableId
https://ESM_URL/rs/esm/v2/help/types/EsmVariableType
https://ESM_URL/rs/esm/v2/help/types/EsmVariableValue
https://ESM_URL/rs/esm/v2/help/types/EsmWatchlist
https://ESM_URL/rs/esm/v2/help/types/EsmWatchlistDetails
https://ESM_URL/rs/esm/v2/help/types/EsmWatchlistField
https://ESM_URL/rs/esm/v2/help/types/EsmWatchlistFile
https://ESM_URL/rs/esm/v2/help/types/EsmWatchlistId
https://ESM_URL/rs/esm/v2/help/types/EsmWatchlistIds
https://ESM_URL/rs/esm/v2/help/types/EsmWatchlistValue
https://ESM_URL/rs/esm/v2/help/types/EsmZone
https://ESM_URL/rs/esm/v2/help/types/EsmZoneId
https://ESM_URL/rs/esm/v2/help/types/EsmZoneInfo
https://ESM_URL/rs/esm/v2/help/types/EsmZoneInfoIn
https://ESM_URL/rs/esm/v2/help/types/EsmZoneInfoOut
https://ESM_URL/rs/esm/v2/help/types/EsmZoneRange
https://ESM_URL/rs/esm/v2/help/types/IpsId
https://ESM_URL/rs/esm/v2/help/types/JobStatusValue
https://ESM_URL/rs/esm/v2/help/types/JsonString
https://ESM_URL/rs/esm/v2/help/types/MActiveResponseAndFilter
https://ESM_URL/rs/esm/v2/help/types/MActiveResponseFilter
https://ESM_URL/rs/esm/v2/help/types/MActiveResponseFilterElement
https://ESM_URL/rs/esm/v2/help/types/MActiveResponseParams
https://ESM_URL/rs/esm/v2/help/types/MActiveResponseSelect
https://ESM_URL/rs/esm/v2/help/types/NameError
https://ESM_URL/rs/esm/v2/help/types/PolicyRolloutError
https://ESM_URL/rs/esm/v2/help/types/PolicyRolloutResponse
https://ESM_URL/rs/esm/v2/help/types/Privilege
https://ESM_URL/rs/esm/v2/help/types/TagGroup
https://ESM_URL/rs/esm/v2/help/types/WriteRollDatasourceResponse
```