# Minnesota Public Records Sources for Research

## Verified Sources (Tested with Firecrawl)

### People Search / Property Records
| Source | URL | Data Available | Firecrawl Status |
|--------|-----|---------------|------------------|
| ClustrMaps | `clustrmaps.com/persons/NAME` | Address history, co-residents, property values, business registrations | ✅ Works well |
| Spokeo | `spokeo.com/STATE/CITY/ADDRESS` | Property details, resident history (redacted), tax records | ✅ Works, heavily redacted |
| FastPeopleSearch | `fastpeoplesearch.com` | Phone, address, age, relatives | ⚠️ Often CAPTCHA-blocked |

### Criminal / Arrest Records
| Source | URL | Data Available | Firecrawl Status |
|--------|-----|---------------|------------------|
| Minnesota Arrests.org | `minnesota.arrests.org/Arrests/NAME_ID/` | Mugshots, charges, arresting agency, date, age at arrest | ✅ Works well |
| Mugshots.com | `mugshots.com/US-States/Minnesota/COUNTY/CITY/NAME.ID.html` | Booking details, charges, release status | ✅ Works |
| MyLife | `mylife.com/NAME/ID` | Criminal/court record flags, address history, associates | ✅ Works, aggregated data |

### Official Government Sources
| Source | URL | Data Available | Notes |
|--------|-----|---------------|-------|
| Minnesota Court Records Online (MCRO) | `publicaccess.courts.state.mn.us` | Court case search | Requires case number or name search via web UI |
| Ramsey County Jail Roster | `ramseycountymn.gov` / `opendata.ramseycountymn.gov` | In-custody bookings | Open data portal available |
| Minnesota Secretary of State | `sos.state.mn.us` | Business entity search | For verifying "{Business Name}" type registrations |

## Area Codes for Geographic Context
| Area Code | Region |
|-----------|--------|
| 651 | Saint Paul, Minnesota |
| 612 | Minneapolis, Minnesota |
| 952 | Southwest suburbs (Eden Prairie, Bloomington) |
| 512 | Austin/Round Rock, Texas |
| 325 | Snyder, Texas (west-central) |

## Key Learning: Cross-State Research
When a subject has a phone number with an out-of-state area code (e.g., 512 Texas number on a Minnesota resident):
1. Search for the name in the area code's state
2. Check for family connections or prior residency
3. Note it as a potential lead, not a data error
