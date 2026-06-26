/**
 * ReMaker AI — Raccolta Feedback Beta
 *
 * ISTRUZIONI:
 * 1. Apri Google Drive → crea un nuovo Google Sheet (es. "ReMaker Feedback Beta")
 * 2. Nel Sheet, vai su Estensioni → Apps Script
 * 3. Cancella il codice di default e incolla TUTTO questo file
 * 4. Salva (Ctrl+S)
 * 5. Clicca "Deploy" → "New deployment"
 *    - Type: Web app
 *    - Execute as: Me
 *    - Who has access: Anyone
 * 6. Autorizza l'app quando richiesto
 * 7. Copia l'URL generato
 * 8. In remaker-test.html, sostituisci 'INSERISCI_QUI_URL_APPS_SCRIPT'
 *    con quell'URL (rimani nelle virgolette singole)
 */

const SHEET_NAME = 'Feedback';

function doGet(e) {
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();

    // Crea il foglio "Feedback" se non esiste
    let sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      // Intestazioni
      sheet.appendRow([
        'Data/Ora',
        'Oggetto Analizzato',
        'Stelle (1-5)',
        'Risultato Accurato',
        'Lo Useresti',
        'Lo Consiglieresti',
        'Suggerimento per migliorare',
        'Cosa non è piaciuto'
      ]);
      // Formatta intestazioni
      const header = sheet.getRange(1, 1, 1, 7);
      header.setFontWeight('bold');
      header.setBackground('#1E2B1F');
      header.setFontColor('#F0E9D8');
    }

    // Leggi parametri URL
    const p = e.parameter;

    // Converti timestamp ISO in data leggibile
    const ts = p.timestamp
      ? new Date(p.timestamp).toLocaleString('it-IT', { timeZone: 'Europe/Rome' })
      : new Date().toLocaleString('it-IT', { timeZone: 'Europe/Rome' });

    // Aggiungi riga
    sheet.appendRow([
      ts,
      p.oggetto        || '',
      p.stelle         || 0,
      p.accurato       || '',
      p.lo_useresti    || '',
      p.consiglieresti || '',
      p.suggerimento   || '',
      p.non_piaciuto   || ''
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Funzione di test — eseguila dalla barra Apps Script per verificare
function testGet() {
  const fakeEvent = {
    parameter: {
      timestamp: new Date().toISOString(),
      oggetto: 'iPhone 11 rotto',
      stelle: '4',
      accurato: 'sì',
      lo_useresti: 'sì',
      consiglieresti: 'sì',
      commento: 'Ottimo! Le idee di riuso erano molto pertinenti.'
    }
  };
  const result = doGet(fakeEvent);
  Logger.log(result.getContent());
}
