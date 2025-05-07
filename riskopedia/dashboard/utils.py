import json
import requests
import json
import wikipedia
import re
from together import Together
import csv
from datetime import datetime
import io

# Initialize the LLM client
client = Together(
    api_key="f8ea0940653a1ddb24d8b5696354ecb9450365d0f1ac68e0ddd2095130faf0d2"
)

sanctioned_countries = [
    "Afghanistan",
    "Belarus",
    "Bosnia and Herzegovina",
    "Burma (Myanmar)",
    "Central African Republic",
    "China",
    "Crimea",
    "Cuba",
    "Cyprus",
    "Democratic People's Republic of Korea (North Korea)",
    "Democratic Republic of the Congo",
    "Donetsk",
    "Eritrea",
    "Ethiopia",
    "Haiti",
    "Hong Kong",
    "ISIL (Da'esh) and Al-Qaida organizations",
    "Iran",
    "Iraq",
    "Lebanon",
    "Libya",
    "Luhansk",
    "Mali",
    "Myanmar (Burma)",
    "Nicaragua",
    "North Korea",
    "Russia",
    "Somalia",
    "South Sudan",
    "Sudan",
    "Syria",
    "Venezuela",
    "Yemen",
    "Zimbabwe",
]

response = [
    {
        "transaction_data": {
            "transaction_id": "TXN-2024-1X3Y",
            "date": "2024-02-10T11: 45: 00Z",
            "sender": {
                "name": "Microsoft Corporation",
                "account": {
                    "iban": "US89 1234 5678 9012 3456 78",
                    "bank_country": "USA",
                },
                "address": "One Microsoft Way, Redmond, WA, USA",
                "notes": "Quarterly software licensing fees for enterprise solutions",
            },
            "receiver": {
                "name": "Tata Consultancy Services (TCS)",
                "account": {
                    "number": "IN98 7654 3210 9876 5432 10",
                    "bank": "State Bank of India, India",
                },
                "address": "TCS House, Mumbai, India",
                "tax_id": "IN-58947",
            },
            "amount": {"value": 12500000.0, "currency": "USD"},
            "transaction_type": "Wire Transfer",
            "reference": "Enterprise Software Solutions - Invoice #MSFT-2024-Q1",
            "additional_notes": [
                "Authorized by CFO Amy Hood.",
                "Routine business payment for IT consulting services.",
            ],
        },
        "sender_wikipedia": "Microsoft Corporation is an American multinational technology conglomerate headquartered in Redmond, Washington. Founded in 1975, the company became highly influential in the rise of personal computers through software like Windows, and the company has since expanded to Internet services, cloud computing, video gaming and other fields. Microsoft is the largest software maker, one of the most valuable public U.S. companies, and one of the most valuable brands globally.\nMicrosoft was founded by Bill Gates and Paul Allen to develop and sell BASIC interpreters for the Altair 8800. It rose to dominate the personal computer operating system market with MS-DOS in the mid-1980s, followed by Windows. During the 41 years from 1980 to 2021 Microsoft released 9 versions of MS-DOS with a median frequency of 2 years, and 13 versions of Windows with a median frequency of 3 years. The company's 1986 initial public offering (IPO) and subsequent rise in its share price created three billionaires and an estimated 12,000 millionaires among Microsoft employees. Since the 1990s, it has increasingly diversified from the operating system market. Steve Ballmer replaced Gates as CEO in 2000.  He oversaw the then-largest of Microsoft's corporate acquisitions in Skype Technologies in 2011, and an increased focus on hardware that led to its first in-house PC line, the Surface, in 2012, and the formation of Microsoft Mobile through Nokia.",
        "receiver_wikipedia": "Tata Consultancy Services (TCS) is an Indian multinational technology company specializing in information technology services and consulting. Headquartered in Mumbai, it is a part of the Tata Group and operates in 150 locations across 46 countries. It is the second-largest Indian company by market capitalization.\nAs of 2024, TCS is ranked seventh on the Fortune India 500 list. In September 2021, TCS recorded a market capitalization of US$200 billion, making it the first Indian IT company to achieve this valuation. In 2012, it was the world's second-largest user of U.S. H-1B visas.  \nIn 2024, parent company Tata Sons owned 71.74% of TCS, and close to 80% of Tata Sons' dividend income came from TCS.\n\n\n== History ==\n\n\n=== 1968–2000 ===\n\nTata Consultancy Services Limited, originally known as Tata Computer Systems, was established in 1968 by Tata Sons Limited. The company's initial contracts involved providing punched card services to its sister company TISCO (now Tata Steel), developing an Inter-Branch Reconciliation System for the Central Bank of India, and offering bureau services to the Unit Trust of India.\nIn 1975, TCS implemented an electronic depository and trading system named SECOM for Swiss company SIS SegaInterSettle. It also developed System X for the Canadian Depository System and automated the Johannesburg Stock Exchange.",
        "sender_country": "United States",
        "receiver_country": "India",
        "risk_analysis": {
            "overall_risk_score": 220,
            "risk_category": "Medium Risk",
            "detailed_justification": "The transaction is considered medium-risk due to the reputable sender and receiver entities, but the sender country (USA) is not a high-risk jurisdiction, and the receiver country (India) is not sanctioned. However, the flagged notes indicate a potential risk due to the routine business payment and authorized by CFO notes.",
            "risk_scores": {
                "sender_entity_reputation": 50,
                "receiver_entity_reputation": 50,
                "sender_country_risk": 0,
                "receiver_country_risk": 0,
                "flagged_notes_risk": 120,
            },
        },
    },
    {
        "transaction_data": {
            "transaction_id": "TXN-2024-4Z9P",
            "date": "2024-01-22T16: 30: 00Z",
            "sender": {
                "name": "Gazprom",
                "account": {
                    "iban": "RU67 4456 3321 0987 6543 21",
                    "bank_country": "Russia",
                },
                "address": "16 Nametkina Street, Moscow, Russia",
                "notes": "Investment in energy infrastructure projects",
            },
            "receiver": {
                "name": "GBC Holdings Ltd",
                "account": {
                    "number": "765432198",
                    "bank": "FirstCaribbean International Bank, Barbados",
                },
                "address": "P.O. Box 3421, Bridgetown, Barbados",
                "tax_id": "BB-99832",
            },
            "amount": {"value": 8750000.0, "currency": "USD"},
            "transaction_type": "Wire Transfer",
            "reference": "Infrastructure Development Agreement - Ref #GBC-2024",
            "additional_notes": [
                "Authorized by Vladimir Lisin (Director).",
                "Fund movement flagged for review due to high-risk jurisdiction.",
                "Intermediary company registered in Seychelles.",
            ],
        },
        "sender_wikipedia": "PJSC Gazprom (Russian: Газпром, IPA: [ɡɐsˈprom]) is a Russian majority state-owned multinational energy corporation headquartered in the Lakhta Center in Saint Petersburg. The Gazprom name is a contraction of the Russian words gazovaya promyshlennost (газовая промышленность, gas industry). In January 2022, Gazprom displaced Sberbank from the first place in the list of the largest company in Russia by market capitalization. In 2023, the company's revenue amounted to 8.5 trillion rubles, a significant decline from the 11.7 trillion rubles it reported in 2022. \nGazprom is vertically integrated and is active in every area of the gas industry, including exploration and production, refining, transport, distribution and marketing, and power generation. In 2018, Gazprom produced twelve percent of the global output of natural gas, producing 497.6 billion cubic meters of natural and associated gas and 15.9 million tonnes of gas condensate. By 2023, this share plunged to  Gazprom then exports the gas through pipelines that the company builds and owns across Russia and abroad, such as Power of Siberia and TurkStream. It produced 359 billion cubic meters of natural and associated gas, a decline of approximately 13 percent from the previous year.In the same year, Gazprom has proven reserves of 35.1 trillion cubic meters of gas and 1.6 billion tons of gas condensate. Gazprom is also a large oil producer through its subsidiary Gazprom Neft, producing about 41 million tons of oil with reserves amounting to 2 billion tons. The company also has subsidiaries in industrial sectors, including finance, media and aviation, and majority stakes in other companies.",
        "receiver_wikipedia": "Cosmo Films (Now Cosmo First Limited) is an Indian multinational corporation that manufactures bi-axially oriented polypropylene films (BOPP) for packaging, label, lamination and industrial applications. The company is headquartered in New Delhi, India. Its manufacturing units are situated in India and South Korea. The company is listed on the Bombay Stock Exchange (BSE) and National Stock Exchange (NSE), India. Mr. Ashok Jaipuria founded Cosmo Films Limited in October 1976 and set up the first production plant at Aurangabad, Maharashtra in the year 1981. In 2001, Cosmo Films acquired a 76.51% stake in Gujarat Propack Limited. In 2009, Cosmo Films acquired US-based GBC Commercial Print Finishing for USD 17.1 million (about Rs. 82 crore).\n\n\n== Operations ==\nCosmo Films major subsidiaries:\n\nCosmo Films Korea Limited.",
        "sender_country": "Russia",
        "receiver_country": "Barbados",
        "risk_analysis": {
            "overall_risk_score": 350,
            "risk_category": "Medium Risk",
            "detailed_justification": "The transaction is flagged for review due to the high-risk jurisdiction of the receiver country, Barbados. Additionally, the sender entity, Gazprom, has a mixed reputation with some negative media coverage and regulatory issues.",
            "risk_scores": {
                "sender_entity_reputation": 60,
                "receiver_entity_reputation": 0,
                "sender_country_risk": 0,
                "receiver_country_risk": 80,
                "flagged_notes_risk": 50,
            },
        },
    },
    {
        "transaction_data": {
            "transaction_id": "TXN-2024-6D3K",
            "date": "2024-03-05T09: 15: 00Z",
            "sender": {
                "name": "Bill & Melinda Gates Foundation",
                "account": {
                    "iban": "US23 6574 8392 1234 0987 22",
                    "bank_country": "USA",
                },
                "address": "500 Fifth Avenue North, Seattle, WA, USA",
                "notes": "Donation for malaria prevention program",
            },
            "receiver": {
                "name": "World Health Organization (WHO)",
                "account": {
                    "number": "CH45 1234 5678 9012 3456 00",
                    "bank": "UBS Bank",
                },
                "address": "Avenue Appia 20, Geneva, Switzerland",
                "tax_id": "CH-98123",
            },
            "amount": {"value": 25000000.0, "currency": "USD"},
            "transaction_type": "Wire Transfer",
            "reference": "Global Health Initiative - Grant #WHO-2024",
            "additional_notes": [
                "Approved by Melinda French Gates.",
                "Routine philanthropic contribution.",
            ],
        },
        "sender_wikipedia": "The Gates Foundation is an American private foundation founded by Bill Gates and Melinda French Gates. Based in Seattle, Washington, it was launched in 2000 and is reported to be the third largest charitable foundation in the world, holding $69 billion in assets as of 2020. The primary stated goals of the foundation are to enhance healthcare and reduce extreme poverty across the world, and to expand educational opportunities and access to information technology in the U.S. Key individuals of the foundation include Warren Buffett, chief executive officer Mark Suzman, and Michael Larson.\nThe BMGF had an endowment of approximately $75.2 billion as of December 31, 2023. The scale of the foundation and the way it seeks to apply business techniques to giving makes it one of the leaders in venture philanthropy, though the foundation itself notes that the philanthropic role has limitations. In 2007, its founders were ranked as the second most generous philanthropists in the U.S., behind Warren Buffett. As of 2018, Bill Gates and Melinda French Gates had donated around $36 billion to the foundation. Since its founding, the foundation has endowed and supported a broad range of social, health, and education developments, including the establishment of the Gates Cambridge Scholarships at Cambridge University.\n\n\n== History ==\n\nIn 1994, the foundation was formed as the William H. Gates Foundation. In May 2002, the foundation purchased stocks in pharmaceutical companies Johnson & Johnson, Merck, and Pfizer.",
        "receiver_wikipedia": 'The World Health Organization (WHO) is a specialized agency of the United Nations responsible for global public health. It is headquartered in Geneva, Switzerland, and has six regional offices and 150 field offices worldwide. Only sovereign states are eligible to join, and it is the largest intergovernmental health organization at the international level.\nThe WHO"s purpose is to achieve the highest possible level of health for all the world"s people, defining health as a state of complete physical, mental and social well-being and not merely the absence of disease or infirmity. The main functions of the World Health Organization include promoting the control of epidemic and endemic diseases; providing and improving the teaching and training in public health, the medical treatment of disease, and related matters; and promoting the establishment of international standards for biological products.\nThe WHO was established on 7 April 1948, and formally began its work on 1 September 1948. It incorporated the assets, personnel, and duties of the League of Nations" Health Organization and the Paris-based Office International d"Hygiène Publique, including the International Classification of Diseases (ICD). The agency"s work began in earnest in 1951 after a significant infusion of financial and technical resources.\nThe WHO"s official mandate is to promote health and safety while helping the vulnerable worldwide. It provides technical assistance to countries, sets international health standards, collects data on global health issues, and serves as a forum for scientific or policy discussions related to health. Its official publication, the World Health Report, provides assessments of worldwide health topics.',
        "sender_country": "United States",
        "receiver_country": "Switzerland",
        "risk_analysis": {
            "overall_risk_score": 120,
            "risk_category": "Low Risk",
            "detailed_justification": "The Bill & Melinda Gates Foundation has a strong reputation, but the transaction amount is significant. The World Health Organization is a reputable entity, but Switzerland is not on the FATF Grey List. The transaction notes are routine and do not indicate any suspicious activity.",
            "risk_scores": {
                "sender_entity_reputation": 80,
                "receiver_entity_reputation": 40,
                "sender_country_risk": 0,
                "receiver_country_risk": 20,
                "flagged_notes_risk": 20,
            },
        },
    },
    {
        "transaction_data": {
            "transaction_id": "TXN-2024-9B7T",
            "date": "2024-02-28T14: 10: 00Z",
            "sender": {
                "name": "Bank Melli Iran",
                "account": {
                    "iban": "IR45 9876 5432 1098 7654 32",
                    "bank_country": "Iran",
                },
                "address": "Ferdowsi Avenue, Tehran, Iran",
                "notes": "Import payment for medical equipment",
            },
            "receiver": {
                "name": "UAE Free Trade Logistics",
                "account": {"number": "234567890", "bank": "Dubai Islamic Bank, UAE"},
                "address": "Al Jaddaf, Dubai, UAE",
                "tax_id": "AE-34872",
            },
            "amount": {"value": 2500000.0, "currency": "USD"},
            "transaction_type": "Wire Transfer",
            "reference": "Medical Equipment Import - Ref #UAE-MED-2024",
            "additional_notes": [
                "Transaction reviewed due to US OFAC restrictions on Iranian entities.",
                "Involves front company in UAE with unclear beneficial ownership.",
            ],
        },
        "sender_wikipedia": 'Bank Melli Iran (BMI; Persian: بانک ملی ایران, romanized: Bânk-e Melli-ye Irân, lit.\u2009"National Bank of Iran") is the first national and commercial retail bank of Iran. It was considered as the largest Iranian company in terms of annual income with a revenue of 364 657 billion Rials in 2016. It is the largest bank in the Islamic world and in the Middle East. By the end of 2016, BMI had a net asset of $76.6 billion and a network of 3.328 banking branches; so it was known as the largest Iranian bank based on the amount of assets. The brand of BMI was recognized as one of the 100 top Iranian brands in 10th National Iranian Heroes Championship in 2013. The National Bank has 3328 active branches inside, 14 active branches and 4 sub-stations abroad, and it has 180 booths. The first managing director of BMI was Kurt Lindenblatt from Germany, the first foreign branch of BMI was opened in Hamburg, Germany in 1948.\n\n\n== History ==\nThe formation of a new bank was first proposed by Haj Mohammad Hassan Amin Dar al-Zarb known as Amināl-Zarb (one of the Tehran stockholders) in 1879 ten years before the creation of the King Bank, to Naser-al-Din Shah Qajar. But this proposal was not accepted with the interference of the countries that dominated Iran and their agents. Instead, the King Bank was established in Iran.',
        "receiver_wikipedia": "Free-trade zones in the United Arab Emirates are areas that have a special tax, customs and import regime, and are governed by their own framework of regulations (with the exception of UAE criminal law).\n\n\n== Background ==\nThe UAE has a number of free zones across Dubai, Abu Dhabi, Sharjah, Fujairah, Ajman, Ras al-Khaimah and Umm al-Quwain. Free zones may be broadly categorized as seaport free zones, airport free zones, and mainland free zones. Free-trade zone exemptions are:\n\n100% foreign ownership of the enterprise\n100% import and export tax exemptions\n100% repatriation of capital and profits\nCorporate tax exemptions for up to 50 years\nNo personal income taxes\nAssistance with labor recruitment, and additional support services, such as sponsorship and housing.\nEach Free Zone is designed around one or more strict industry categories. An independent Free Zone Authority (FZA) governs each free zone, and is the agency responsible for issuing FTZ operating licenses and assisting companies with establishing their business in the FTZ. Each free zone has its own specific requirements regarding minimum capital requirements, office or warehouse space and permitted activities; with each possessing the relevant licenses and adequate legislation to enable their dedicated industry to flourish.\nInvestors can either register a new company in the form of a Free Zone Establishment (FZE) or simply establish a branch or representative office of their existing or parent company based within the UAE or abroad. An FZE is a limited liability company governed by the rules and regulations of the Free Zone in which it is established. Except for acquiring nationality in the UAE, the provisions of the Commercial Companies Law (CCL) do not apply to FZEs, provided that the Free Zones have special provisions regulating such companies.\nFree zone companies can run business within the relevant zone or outside the UAE. Some free zones (including ADGM, JAFZA, DMCC, RAK FTZ) allow for inward redomiciliation of foreign companies, which means a transfer of a corporate seat of an existing company from abroad to the UAE free zone.",
        "sender_country": "Iran",
        "receiver_country": "United Arab Emirates",
        "risk_analysis": {
            "overall_risk_score": 420,
            "risk_category": "High Risk",
            "detailed_justification": "The transaction involves a sender entity with a questionable reputation, as it is an Iranian bank subject to US OFAC restrictions. The receiver entity is a free trade zone company in the UAE, which may have unclear beneficial ownership. The transaction notes indicate that the transaction was reviewed due to US OFAC restrictions and involves a front company in the UAE.",
            "risk_scores": {
                "sender_entity_reputation": 80,
                "receiver_entity_reputation": 40,
                "sender_country_risk": 100,
                "receiver_country_risk": 20,
                "flagged_notes_risk": 80,
            },
        },
    },
    {
        "transaction_data": {
            "transaction_id": "TXN-2024-2M8X",
            "date": "2024-03-10T18: 50: 00Z",
            "sender": {
                "name": "Deutsche Bank AG",
                "account": {
                    "iban": "DE79 5007 0010 1234 5678 90",
                    "bank_country": "Germany",
                },
                "address": "Taunusanlage 12, Frankfurt, Germany",
                "notes": "Corporate investment fund disbursement",
            },
            "receiver": {
                "name": "Omega Capital Ventures Ltd",
                "account": {"number": "675849302", "bank": "Butterfield Bank, Bermuda"},
                "address": "65 Front Street, Hamilton, Bermuda",
                "tax_id": "BM-56478",
            },
            "amount": {"value": 15250000.0, "currency": "USD"},
            "transaction_type": "Wire Transfer",
            "reference": "Investment Fund Allocation - Ref #OMEGA-2024",
            "additional_notes": [
                "Authorized by CFO Christian Sewing.",
                "Transaction structure raised red flags due to offshore beneficiary location.",
                "Linked to prior transactions involving shell companies in the Cayman Islands.",
            ],
        },
        "sender_wikipedia": 'Deutsche Bank AG (German pronunciation: [ˈdɔʏtʃə ˈbaŋk ʔaːˈɡeː lit.\u2009"German Bank") is a German multinational investment bank  and financial services company headquartered in Frankfurt, Germany, and dual-listed on the Frankfurt Stock Exchange and the New York Stock Exchange.\nDeutsche Bank was founded in 1870 in Berlin. From 1929 to 1937, following its merger with Disconto-Gesellschaft, it was known as Deutsche Bank und Disconto-Gesellschaft or DeDi-Bank.:\u200a580\u200a Other transformative acquisitions have included those of Mendelssohn & Co. in 1938, Morgan Grenfell in 1990, Bankers Trust in 1998, and Deutsche Postbank in 2010.\nAs of 2018, the bank"s network spanned 58 countries with a large presence in Europe, the Americas, and Asia. It is a component of the DAX stock market index and is often referred to as the largest German banking institution, with Deutsche Bank holding the majority stake in DWS Group for combined assets of 2.2 trillion euros, rivaling even Sparkassen-Finanzgruppe in terms of combined assets.\nDeutsche Bank has been designated a global systemically important bank by the Financial Stability Board since 2011. It has been designated as a Significant Institution since the entry into force of European Banking Supervision in late 2014, and as a consequence is directly supervised by the European Central Bank.\nAccording to a 2020 article in the New Yorker, Deutsche Bank had long had an "abject" reputation among major banks, as it has been involved in major scandals across various issue areas.\n\n\n== History ==\n\n\n=== 1870–1933 ===\nDeutsche Bank was founded in 1870 in Berlin as a specialist bank for financing foreign trade and promoting German exports.',
        "receiver_wikipedia": "An international joint venture (IJV) occurs when two businesses based in two or more countries form a partnership. A company that wants to explore international trade without taking on the full responsibilities of cross-border business transactions has the option of forming a joint venture with a foreign partner. International investors entering into a joint venture minimize the risk that comes with an outright acquisition of a business. In international business development, performing due diligence on the foreign country and the partner limits the risks involved in such a business transaction.\nIJVs aid companies to form strategic alliances, which allow them to gain competitive advantage through access to a partner's resources, including markets, technologies, capital and people. International joint ventures are viewed as a practical vehicle for knowledge transfer, such as technology transfer, from multinational expertise to local companies, and such knowledge transfer can contribute to the performance improvement of local companies. Within IJVs one or more of the parties is located where the operations of the IJV take place and also involve a local and foreign company.\n\n\n== Basic elements ==\nThese include:\n\nContractual Agreement - IJVs are established by express contracts that consist of one or more agreements involving two or more individuals or organizations and that are entered into for a specific business purpose.\nSpecific Limited Purpose and Duration - IJVs are formed for a specific business objective and can have a limited life span or be long-term. IJVs are frequently established for a limited duration because (a) the complementary activities involve a limited amount of assets; (b) the complementary assets have only a limited service life; and/or (c) the complementary production activities will be of only limited efficacy.",
        "sender_country": "Germany",
        "receiver_country": "Bermuda",
        "risk_analysis": {
            "overall_risk_score": 420,
            "risk_category": "High",
            "detailed_justification": "The transaction involves a German bank with a history of scandals and a Bermuda-based entity with no clear reputation. The transaction notes raise red flags due to the offshore beneficiary location and link to prior transactions involving shell companies.",
            "risk_scores": {
                "sender_entity_reputation": 80,
                "receiver_entity_reputation": 0,
                "sender_country_risk": 0,
                "receiver_country_risk": 50,
                "flagged_notes_risk": 90,
            },
        },
    },
]


def transformResponse(response):
    entity_risks = []
    geo_risks = []
    transactions = []
    incidentRiskCategoryValues = [0, 0, 0]
    totalRisk = 0
    for transaction in response:
        entity_risks.append(
            [
                transaction["risk_analysis"]["risk_scores"]["sender_entity_reputation"],
                transaction["transaction_data"]["sender"]["name"],
            ]
        )
        entity_risks.append(
            [
                transaction["risk_analysis"]["risk_scores"][
                    "receiver_entity_reputation"
                ],
                transaction["transaction_data"]["receiver"]["name"],
            ]
        )

        geo_risks.append(
            [
                transaction["risk_analysis"]["risk_scores"]["sender_country_risk"],
                transaction["sender_country"],
            ]
        )
        geo_risks.append(
            [
                transaction["risk_analysis"]["risk_scores"]["receiver_country_risk"],
                transaction["receiver_country"],
            ]
        )

        transaction["risk_analysis"]["overall_risk_score"] = calculate_weighted_risk(
            transaction["risk_analysis"]["risk_scores"]
        )

        transaction["risk_analysis"]["detailed_justification"] = transaction[
            "risk_analysis"
        ]["detailed_justification"].replace("'", "")

        riskCategory = ""
        if transaction["risk_analysis"]["overall_risk_score"] < 40:
            riskCategory = "low"
            incidentRiskCategoryValues[0] += 1
        elif 40 <= transaction["risk_analysis"]["overall_risk_score"] < 60:
            riskCategory = "medium"
            incidentRiskCategoryValues[1] += 1
        else:
            riskCategory = "high"
            incidentRiskCategoryValues[2] += 1
        # if "low" in transaction["risk_analysis"]["risk_category"].lower():
        #     riskCategory = "low"
        #     incidentRiskCategoryValues[0] += 1
        # elif "medium" in transaction["risk_analysis"]["risk_category"].lower():
        #     riskCategory = "medium"
        #     incidentRiskCategoryValues[1] += 1
        # elif "high" in transaction["risk_analysis"]["risk_category"].lower():
        #     riskCategory = "high"
        #     incidentRiskCategoryValues[2] += 1
        # else:
        #     riskCategory = "low"
        #     incidentRiskCategoryValues[0] += 1

        totalRisk += transaction["risk_analysis"]["overall_risk_score"]
        transactions.append(
            {
                "transaction_id": transaction["transaction_data"]["transaction_id"],
                "amount": f'{transaction["transaction_data"]["amount"]["value"]} {transaction["transaction_data"]["amount"]["currency"]}',
                "risk_score": transaction["risk_analysis"]["overall_risk_score"],
                "risk_category": riskCategory,
                "detailed_justification": transaction["risk_analysis"][
                    "detailed_justification"
                ],
                "individual_risk_scores": [
                    transaction["risk_analysis"]["risk_scores"][
                        "sender_entity_reputation"
                    ],
                    transaction["risk_analysis"]["risk_scores"]["sender_country_risk"],
                    transaction["risk_analysis"]["risk_scores"][
                        "receiver_entity_reputation"
                    ],
                    transaction["risk_analysis"]["risk_scores"][
                        "receiver_country_risk"
                    ],
                    transaction["risk_analysis"]["risk_scores"]["flagged_notes_risk"],
                ],
                "sender_entity_type": transaction["risk_analysis"]["corporation_type"][
                    "sender"
                ],
                "receiver_entity_type": transaction["risk_analysis"][
                    "corporation_type"
                ]["receiver"],
                "references": [
                    transaction["sender_wikipedia_url"],
                    transaction["receiver_wikipedia_url"],
                    transaction["sender_news_urls"],
                    transaction["receiver_news_urls"],
                ],
            }
        )

    entity_risks.sort(reverse=True)
    topRiskOrgs = []
    topRiskValues = []
    otherSum = 0
    for idx in range(len(entity_risks)):
        if idx < 4:
            topRiskOrgs.append(entity_risks[idx][1])
            topRiskValues.append(entity_risks[idx][0])
        else:
            otherSum += entity_risks[idx][0]

    topRiskOrgs.append("Others")
    topRiskValues.append(otherSum)

    geo_risks.sort(reverse=True)
    geoRiskCountries = []
    geoRiskValues = []
    otherSum = 0
    for idx in range(len(geo_risks)):
        if idx < 4:
            geoRiskCountries.append(geo_risks[idx][1])
            geoRiskValues.append(geo_risks[idx][0])
        else:
            otherSum += entity_risks[idx][0]

    geoRiskCountries.append("Others")
    geoRiskValues.append(otherSum)

    totalRisk /= len(transactions)

    context = {
        "totalAvgRiskScore": int(totalRisk),
        "geoRiskCountries": geoRiskCountries,
        "geoRiskValues": geoRiskValues,
        "incidentRiskCategoryValues": incidentRiskCategoryValues,
        "topRiskOrgs": topRiskOrgs,
        "topRiskValues": topRiskValues,
        "transactions": transactions,
    }

    return context


# ----------------------- Step 1: Read Transactions from File ----------------------- #
def read_transactions_from_file(file_path):
    """Reads a file containing multiple transactions separated by '---'."""
    with open(file_path, "r", encoding="utf-8") as file:
        transactions_text = file.read().strip()

    return transactions_text.split("\n---\n")


def read_transactions_from_file2(file_content):
    """Reads a file containing multiple transactions separated by '---'."""

    transactions_text = file_content.strip()

    return transactions_text.split("\r\n---\r\n")


def process_csv(csv_content):
    transactions = []

    # Use StringIO to treat the string content as a file
    file = io.StringIO(csv_content)
    reader = csv.DictReader(file)

    for row in reader:
        # Extract and clean the amount field
        raw_amount = row.get("Amount", "").strip()
        amount_value = 0.0  # Default if empty

        if raw_amount:
            # Remove non-numeric characters except for the decimal point
            cleaned_amount = re.sub(r"[^\d.]", "", raw_amount)

            # Ensure only one decimal point exists
            if cleaned_amount.count(".") > 1:
                cleaned_amount = cleaned_amount.replace(
                    ".", "", cleaned_amount.count(".") - 1
                )

            try:
                amount_value = float(cleaned_amount)
            except ValueError:
                amount_value = 0.0  # Fallback if conversion fails

        # Convert date to ISO format
        date_str = row.get("Date", "").strip()
        try:
            date_iso = (
                datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").isoformat() + "Z"
                if date_str
                else ""
            )
        except ValueError:
            date_iso = ""

        transaction = {
            "transaction_id": row.get("Transaction ID", "").strip(),
            "date": date_iso,
            "sender": {
                "name": row.get("Payer Name", "").strip(),
                "account": {
                    "iban": row.get("Sender IBAN", "").strip(),
                    "bank_country": row.get("Sender Country", "").strip(),
                },
                "address": row.get("Sender Country", "").strip(),
                "notes": row.get("Sender Notes", "").strip(),
            },
            "receiver": {
                "name": row.get("Receiver Name", "").strip(),
                "account": {
                    "number": row.get("Receiver Account Number", "").strip(),
                    "bank": row.get("Receiver Bank", "").strip(),
                },
                "address": row.get("Receiver Country", "").strip(),
                "tax_id": row.get("Receiver Tax ID", "").strip(),
            },
            "amount": {
                "value": amount_value,
                "currency": row.get("Currency", "").strip(),
            },
            "transaction_type": row.get("Transaction Type", "").strip(),
            "reference": row.get("Reference", "").strip(),
            "additional_notes": (
                row.get("Transaction Details", "").strip().split(";")
                if row.get("Transaction Details", "").strip()
                else []
            ),
        }
        transactions.append(transaction)

    return json.dumps(transactions, indent=2)


def extract_json(response_text):
    """Extracts JSON from a given text response using regex."""
    # print(response_text)
    match = re.search(
        r"\{.*\}", response_text, re.DOTALL
    )  # Capture content between the first and last curly brace
    if match:
        json_str = match.group(0)  # Extract JSON string
        try:
            return json.loads(json_str)  # Validate JSON
        except json.JSONDecodeError:
            print("Error: Extracted JSON is invalid.")
            return None
    print("Error: No JSON found in response.")
    return None


# ----------------------- Step 2: Extract Transaction Details Using LLM ----------------------- #
def extract_transaction_details(transaction):
    """Extracts structured transaction details using an LLM model."""
    try:
        prompt = f"""Extract and structure the following financial transaction details into a JSON format. 
            Identify metadata, sender details, receiver details, financial attributes, and additional notes. 
            Ensure accuracy by preserving entity names, account numbers, amount, transaction type, addresses, and flagged risks. 
            The output must be JSON, with no extra text.

            Input Transaction: {transaction} 

            Output format: 
            {{
              "transaction_id": "string",
              "date": "ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)",
              "sender": {{
                "name": "string",
                "account": {{
                  "iban": "string",
                  "bank_country": "string"
                }},
                "address": "string",
                "notes": "string"
              }},
              "receiver": {{
                "name": "string",
                "account": {{
                  "number": "string",
                  "bank": "string"
                }},
                "address": "string",
                "tax_id": "string"
              }},
              "amount": {{
                "value": float,
                "currency": "string"
              }},
              "transaction_type": "string",
              "reference": "string",
              "additional_notes": ["string"]
            }}
        """

        response = client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stop=["<|eot_id|>"],
            stream=False,
        )

        return extract_json(response.choices[0].message.content)

    except Exception as e:
        print(f"Error extracting entities: {e}")
        return None


# ----------------------- Step 3: Fetch Wikipedia Data ----------------------- #
def get_wikipedia_data(entity_name):
    """Fetches Wikipedia summary for a given entity."""
    try:
        # print(wikipedia.page(entity_name).url)
        return (
            wikipedia.summary(entity_name, sentences=10),
            wikipedia.page(entity_name).url,
        )
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for {entity_name}.", None
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple possible matches: {', '.join(e.options[:3])}.", None
    except Exception as e:
        return f"Error fetching Wikipedia data: {e}", None


# ----------------------- Step 4: Extract Location Data ----------------------- #
def extract_country_from_address(address):
    """Uses OpenAI's LLM to extract country information from an address."""
    try:
        prompt = f"""Extract the country name from the following address:
            Address: {address}
            Output format: {{ "country": "string" }}
        """

        response = client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stream=False,
        )

        return extract_json(response.choices[0].message.content)["country"]

    except Exception as e:
        print(f"Error extracting country from address: {e}")
        return "Unknown"


# # ----------------------- Step 5: Analyze Risk Using LLM ----------------------- #
# def analyze_transaction_risk(
#     transaction_data, sender_wiki, receiver_wiki, sender_country, receiver_country
# ):
#     """Uses LLM to analyze risk based on transaction details and Wikipedia data."""
#     try:
#         prompt = f"""
#           You are a financial crime analyst specializing in risk assessment. Your task is to analyze the following financial transaction for potential risks based on entity reputation, country risk, watchlists, and transaction notes. Your assessment should strictly follow the defined JSON format.

#           ### **Evaluation Criteria (Total: 500 points)**
#           Assign a risk score (0-100) to each factor, with **higher scores indicating higher risk**:
#           1. **Sender Entity Reputation Risk (0-100):** Based on Wikipedia data, fraud history, regulatory violations, or negative media coverage.
#           2. **Receiver Entity Reputation Risk (0-100):** Based on Wikipedia data, fraud history, regulatory violations, or negative media coverage.
#           3. **Sender Country Risk (0-100):** Based on FATF high-risk jurisdictions, OFAC/UN/UK/US sanctions, known terrorist financing activities, corruption index, or tax havens.
#           4. **Receiver Country Risk (0-100):** Based on FATF high-risk jurisdictions, OFAC/UN/UK/US sanctions, known terrorist financing activities, corruption index, or tax havens.
#           5. **Flagged Notes Risk (0-100):** Based on suspicious transaction descriptions (e.g., "urgent", "anonymous", "missing invoice", "offshore entity", "large cash movement", "shell company").

#           ### **Sanctioned Countries & Watchlists**
#           Consider high-risk jurisdictions in the **FATF Blacklist, FATF Grey List, OFAC Sanctions List, UN Sanctions List, and UK High-Risk List**:
#           {sanctioned_countries}

#           ### **Instructions:**
#           1. Assign a score (0-100) for each risk factor using the provided evaluation criteria.
#           2. The **overall risk score** is the sum of the individual risk factors (**maximum score: 500**).
#           3. Categorize the transaction risk level:
#             - **Low Risk (0-150)**
#             - **Medium Risk (151-300)**
#             - **High Risk (301-500)**
#           4. Provide a clear and **detailed justification** for the assigned scores.
#           5. **Ensure the output is always in valid JSON format** with no extra text or explanations.

#           ### **Transaction Data**
#           Transaction Details: {json.dumps(transaction_data, indent=2)}
#           Sender Wikipedia Data: {sender_wiki}
#           Receiver Wikipedia Data: {receiver_wiki}
#           Sender Country: {sender_country}
#           Receiver Country: {receiver_country}

#           ### **Expected Output (Strict JSON Format)**
#           Return ONLY a well-formatted JSON object in the following structure:
#           {{
#             "overall_risk_score": int,
#             "risk_category": "Low | Medium | High",
#             "detailed_justification": "String",
#             "risk_scores": {{
#               "sender_entity_reputation": int,
#               "receiver_entity_reputation": int,
#               "sender_country_risk": int,
#               "receiver_country_risk": int,
#               "flagged_notes_risk": int
#             }}
#           }}

#         """

#         response = client.chat.completions.create(
#             model="meta-llama/Llama-3-8b-chat-hf",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.0,
#             top_p=0.7,
#             top_k=50,
#             repetition_penalty=1,
#             stream=False,
#         )

#         return extract_json(response.choices[0].message.content)

#     except Exception as e:
#         print(f"Error analyzing risk: {e}")
#         return {
#             "risk_score": 0,
#             "risk_category": "unknown",
#             "justification": "Error processing risk analysis.",
#         }


# ----------------------- Step 5: Analyze Risk Using LLM ----------------------- #
def analyze_transaction_risk(
    transaction_data, sender_wiki, receiver_wiki, sender_country, receiver_country
):
    """Uses LLM to analyze risk based on transaction details and Wikipedia data."""
    try:
        prompt = f"""
          You are a financial crime analyst specializing in risk assessment. Your task is to analyze the following financial transaction for potential risks based on entity reputation, country risk, watchlists, and transaction notes. Your assessment should strictly follow the defined JSON format.

          ### *Evaluation Criteria (Total: 500 points)*
          Assign a risk score (0-100) to each factor, with *higher scores indicating higher risk*:
          1. *Sender Entity Reputation Risk (0-100):* Based on Wikipedia data, fraud history, regulatory violations, or negative media coverage.
          2. *Receiver Entity Reputation Risk (0-100):* Based on Wikipedia data, fraud history, regulatory violations, or negative media coverage.
          3. *Sender Country Risk (0-100):* Based on FATF high-risk jurisdictions, OFAC/UN/UK/US sanctions, known terrorist financing activities, corruption index, or tax havens.
          4. *Receiver Country Risk (0-100):* Based on FATF high-risk jurisdictions, OFAC/UN/UK/US sanctions, known terrorist financing activities, corruption index, or tax havens.
          5. *Flagged Notes Risk (0-100):* Based on suspicious transaction descriptions (e.g., "urgent", "anonymous", "missing invoice", "offshore entity", "large cash movement", "shell company").

          ### *Sanctioned Countries & Watchlists*
          Consider high-risk jurisdictions in the *FATF Blacklist, FATF Grey List, OFAC Sanctions List, UN Sanctions List, and UK High-Risk List*:
          {sanctioned_countries}

          ### *Instructions:*
          1. Assign a score (0-100) for each risk factor using the provided evaluation criteria.
          2. The *overall risk score* is the sum of the individual risk factors (*maximum score: 500*).
          3. Categorize the transaction risk level:
            - *Low Risk (0-150)*
            - *Medium Risk (151-300)*
            - *High Risk (301-500)*
          4. Provide a clear and *detailed justification* for the assigned scores.
          5. *Ensure the output is always in valid JSON format* with no extra text or explanations.
          6. Provide the type of corporation the sender and receiving entities are for e.g. Public Limited, Shell Corporation, Offshore Corporation
          Nonprofit Corporation, Limited Liability Partnership, Limited Liability Company etc.
          7. Provide a confidence score for how accurate is the risk scoring for each of the transactions in the "confidence" key in json output.

          ### *Transaction Data*
          Transaction Details: {json.dumps(transaction_data, indent=2)}
          Sender Wikipedia Data: {sender_wiki}
          Receiver Wikipedia Data: {receiver_wiki}
          Sender Country: {sender_country}
          Receiver Country: {receiver_country}
          ### *Recent news articles for the entities or persons involved in the transactions*
          sender news: {recent_news_articles(transaction_data['sender']['name'])}
          receiver news: {recent_news_articles(transaction_data['receiver']['name'])}
          ### *Expected Output (Strict JSON Format)*
          Return ONLY a well-formatted JSON object in the following structure:
          {{
            "overall_risk_score": int,
            "risk_category": "Low | Medium | High",
            "detailed_justification": "String",
            "confidence": float
            "corporation_type": {{
              "sender": "String",
              "receiver": "String"
            }}
            "risk_scores": {{
              "sender_entity_reputation": int,
              "receiver_entity_reputation": int,
              "sender_country_risk": int,
              "receiver_country_risk": int,
              "flagged_notes_risk": int
            }}
          }}

        """

        response = client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stream=False,
        )

        return extract_json(response.choices[0].message.content)

    except Exception as e:
        print(f"Error analyzing risk: {e}")
        return {
            "risk_score": 0,
            "risk_category": "unknown",
            "justification": "Error processing risk analysis.",
        }


def recent_news_articles(entity):
    """Fetches recent news articles related to the given entity and creates a context summary."""
    API_KEY = "1d3035a7be3d4a2bf48a7a48086e18f6"
    url = f"http://api.mediastack.com/v1/news?access_key={API_KEY}&keywords={entity}&countries=us,in"

    try:
        response = requests.get(url)
        # response.raise_for_status()  # Raise an error for HTTP issues
        data = response.json()

        if "pagination" not in data or data["pagination"]["count"] == 0:
            return {"news_urls": [], "context": f"No recent news found for {entity}."}

        articles = data.get("data", [])
        news_urls, context_list = [], []

        for i in range(0, min(len(articles), 5)):  # Limit to 5 articles
            news_urls.append(articles[i].get("url", ""))
            title = articles[i].get("title", "No Title")
            description = articles[i].get("description", "No Description")
            context_list.append(f"- {title}: {description}")

        # Creating a structured context for LLM
        context = f"Recent news for {entity}:\n" + "\n".join(context_list)
        return {"news_urls": news_urls, "context": context}

    except requests.exceptions.RequestException as e:
        # print("Error")
        return {
            "news_urls": [],
            "context": f"Error fetching news for {entity}: {str(e)}",
        }


# ----------------------- Step 6: Execute the Workflow ----------------------- #
def execute(file_path):
    """Main execution function to process transactions."""
    # Step 1: Read input transactions
    print("Reading the input transactions from the file.....")

    input_transactions = read_transactions_from_file2(file_path)

    print("\nProcessing the transactions.....")
    processed_transactions = []
    i = 1
    for transaction in input_transactions:
        # Step 2: Extract structured details
        transaction_data = extract_transaction_details(transaction)
        if not transaction_data:
            continue  # Skip if extraction failed

        # Step 3: Fetch Wikipedia data for sender & receiver
        sender_wiki, sender_url = get_wikipedia_data(transaction_data["sender"]["name"])
        receiver_wiki, receiver_url = get_wikipedia_data(
            transaction_data["receiver"]["name"]
        )

        if sender_url is None:
            sender_url = ""
        if receiver_url is None:
            receiver_url = ""

        # Step 4: Extract sender & receiver country from addresses
        sender_country = extract_country_from_address(
            transaction_data["sender"]["address"]
        )
        receiver_country = extract_country_from_address(
            transaction_data["receiver"]["address"]
        )

        sender_news_urls = recent_news_articles(transaction_data["sender"]["name"])[
            "news_urls"
        ]
        receiver_news_urls = recent_news_articles(transaction_data["receiver"]["name"])[
            "news_urls"
        ]

        if len(sender_news_urls) == 0:
            sender_news_urls

        # print(f"sender urls {sender_news_urls}")
        # print(f"rceiver urls {receiver_news_urls}")

        # Step 5: Perform risk analysis
        risk_analysis = analyze_transaction_risk(
            transaction_data,
            sender_wiki,
            receiver_wiki,
            sender_country,
            receiver_country,
        )

        # Combine all extracted data
        processed_transactions.append(
            {
                "transaction_data": transaction_data,
                "sender_wikipedia": sender_wiki,
                "receiver_wikipedia": receiver_wiki,
                "sender_wikipedia_url": sender_url,
                "receiver_wikipedia_url": receiver_url,
                "sender_news_urls": (
                    sender_news_urls[0] if len(sender_news_urls) > 0 else ""
                ),
                "receiver_news_urls": (
                    receiver_news_urls[0] if len(receiver_news_urls) > 0 else ""
                ),
                "sender_country": sender_country,
                "receiver_country": receiver_country,
                "risk_analysis": risk_analysis,
            }
        )

        print(f"\tCompleted for {i} transactions")
        i += 1

    return processed_transactions


def calculate_weighted_risk(risk_scores):
    """
    Calculate the overall weighted risk score based on assigned weights:
    - Sender entity reputation: 25%
    - Receiver entity reputation: 25%
    - Sender country risk: 20%
    - Receiver country risk: 20%
    - Flagged notes risk: 10%

    :param risk_scores: Dictionary containing individual risk scores.
    :return: Weighted risk score (0-100).
    """

    weights = {
        "sender_entity_reputation": 0.25,
        "receiver_entity_reputation": 0.25,
        "sender_country_risk": 0.20,
        "receiver_country_risk": 0.20,
        "flagged_notes_risk": 0.10,
    }

    weighted_score = sum(risk_scores[key] * weights[key] for key in risk_scores)
    return round(weighted_score, 2)  # Rounding for better readability
