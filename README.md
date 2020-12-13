
# Donations Analysis

- Omar Trejo
- 2020-05-04

## Notes

- A functional approach (e.g. avoid classes as much as possible) will be taken
  to avoid technical programming issues and focus on analysis techniques
- Some of the approaches could be made more complex/improved but the main focus
  here will be to get the basics right and then we can get more fancy

## Tasks

- Project high-level tasks
    - [x] Project structure
    - [x] Analysis questions
    - [x] Data questions / issues
    - [ ] Dictionaries
    - [x] Code setup
    - [x] Data setup
    - [x] Create git repository
    - [ ] Descriptive statistics
    - [ ] Hypothesis tests
    - [ ] Time-series forecasting
    - [ ] Behavior prediction
    - [ ] Automated report

- Rohith tasks
    - [ ] Data dictionaries
    - [ ] Get more data sources (e.g. "Would you donate $500?" info)
    - [ ] Research descriptive statistics and hypothesis testing
    - [ ] Start experimenting with pandas using the repository

## Analysis Questions

- How to identify donors we want to target?
- How to identify small donors over the long run?
- How to target potential new donors (e.g. geography)?
- How do I know my mailing campaigns have worked?

- What is the overall donation tendency? Per state/city/zip?
- Are longer-lasting donators more likely to donate more?
- Are longer-lasting donators more likely to donate less?
- Are higher donators more likely to auto-renew?
- What sources produce the highest donations?

- Data for whether people have been asked to increase their donation amounts?

## Data Questinos / Issues

- Various fields contain `#######` as values (e.g. dates)
- Without transaction dates we can analyze at the month-level (need more files)
- Do we have multiple observations where there shouldn't be?
- Check that`peopleid` and `acctid` are one-to-one and eliminate one
- Check that `CurrentGivingLevelAmt` are one-to-one and eliminate one
- Check that `ZipCode` and `USZipCode` are one-to-one and eliminate one
- There's some missing data (e.g. `NumPlgYears`)
- There are no `LastPaymentDate` values
- What do the values in `AccSts` mean?
- What is `WebPageRespondedto`?
- What is `PmtAmt`?
- What is `AccSts`?
- What is `Zip4`?
- When joining data, use UIDs as well as dates and possibly others?

## Dictionaries

The link between CSVs are `peopleid` and/or `acctid`.

### `Donation_April_2020.csv`

- `WebTransID`
- `SrcCodeDesc`
- `AcctSts`
- `ExpDate`
- `CurrentGivingLevelAmt`
- `LastRenlSrcCode`
- `LastRenlMode`
- `SustPlgFlag`
- `PlgDate`
- `PaidAmt`
- `FundCode`
- `PlgID`
- `PmtID`
- `PmtAmt`
- `PmtDateYear`
- `PeopleID`
- `AcctID`
- `PlgType`
- `SrcCode`
- `SolType`
- `SolMeth`
- `LastCashJournDate`
- `Mode`
- `CCType`
- `PlgSts`

### `Contact_April_2020.csv`

- `ModifiedDate`
- `JobTitle`
- `ZipCode`
- `DATE OF BIRTH`
- `FuncCode`
- `AcctID`
- `PeopleID`
- `EnvSalu`
- `Prefix`
- `FirstName`
- `CurrentGivingLevelAmt`
- `LastName`
- `CompName`
- `Addr`
- `Addr1`
- `City`
- `StateProv`
- `USZipCode`
- `Zip4`
- `TeleNum`
- `EmailAddr`
- `LetterSalu`
- `MajorDonorFlag`
- `OrigJoinDate`
- `ExpDate`
- `LastPaymentDate`
- `AcctSts`
- `MaritalSts`
- `WebPageRespondedto`
- `NumSoftBounces`
- `AddlGiftGiverInd`
- `TotLifetimeGivingAmt`
- `PLANNED GIVING PROSPECT`
- `FAVORITE TYPE OF PROGRAM`
- `WOULD CONSIDER IN ESTATE PLANS`
- `IN ESTATE PLANS`
- `EDUCATION LEVEL`
- `ETHNICITY`
- `BIRTHDATE`
- `BIRTH YEAR`
- `NumPlgYears`
- `SustPlgFlag`
- `HighestPlgAmt`
