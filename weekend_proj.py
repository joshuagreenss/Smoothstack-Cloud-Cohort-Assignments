from openpyxl import load_workbook
import os
import logging
def main():
    m_list = ['january','february','march','april','may','june','july','august','september','october','november','december']
    logging.basicConfig(filename='monthly_report.log',level='INFO')
    f = input("Filename: ")
    toks = f.split("_")
    month = toks[-2]
    year = toks[-1].split('.')[0]
    #Assume relative to running location
    f = os.path.abspath(f)
    try:
        wb = load_workbook(f)
    except:
        logging.error('Invalid filename')
        return
    logging.info(f"Reading for Year {year} Month {month}")
    #If we can find the sheets, we can assume that they are in the right formatting
    try:
        curr_sh = wb['Summary Rolling MoM']
    except:
        logging.error('Summary not found')
    else:
        my_found = False
        for row in curr_sh:
            if row[0].value is None:
                pass
            elif m_list[row[0].value.month-1] == month:
                my_found = True
                logging.info(f"Calls Offered: {row[1].value}")
                logging.info(f"Abandon after 30s: {row[2].value}")
                logging.info(f"FCR %: {row[3].value*100}")
                logging.info(f"DSAT %: {row[4].value*100}")
                logging.info(f"CSAT %: {row[5].value*100}")
                break
        if not my_found:
            logging.warning("Input month/year not found in Summary")
    try:
        curr_sh = wb['VOC Rolling MoM']
    except:
        logging.error('VOC not found')
    else:
        my_found = False
        for c in next(curr_sh.rows):
            if c.value is None:
                pass
            elif m_list[c.value.month-1] == month and c.value.year == int(year):
                my_found = True
                logging.info(f"Base Size: {curr_sh[3][c.column-1].value*100}")
                if curr_sh[3][c.column].value > 200:
                    logging.info("Promoters: Good")
                else:
                    logging.info("Promoters: Bad")
                logging.info(f"Promoters %: {curr_sh[5][c.column-1].value*100}")
                if curr_sh[5][c.column].value > 100:
                    logging.info("Passives: Good")
                else:
                    logging.info("Passives: Bad")
                logging.info(f"Passives %: {str(curr_sh[7][c.column-1].value*100)}")
                if curr_sh[7][c.column].value > 100:
                    logging.info("Detractors: Good")
                else:
                    logging.info("Detractors: Bad")
                logging.info(f"Detractors %: {curr_sh[9][c.column-1].value*100}")
                logging.info(f"Overall NPS%: {curr_sh[13][c.column-1].value*100}")
                logging.info(f"Agent SAT%: {curr_sh[16][c.column-1].value*100}")
                logging.info(f"Agent DSAT%: {curr_sh[19][c.column-1].value*100}")
                break
        if not my_found:
            logging.error("Input month/year not found in VOC")
    
if __name__ == "__main__":
    main()