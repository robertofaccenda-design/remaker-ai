const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, PageBreak,
  LevelFormat, ExternalHyperlink,
} = require('docx');
const fs = require('fs');

// ── Palette ───────────────────────────────────────────────────────────────────
const RUST  = "C0392B";
const DARK  = "1A1A1A";
const GRAY  = "777777";
const LIGHT = "FDF6F0";

// ── Helpers ───────────────────────────────────────────────────────────────────
const sp = (after = 200) =>
  new Paragraph({ children: [new TextRun("")], spacing: { after } });

function t(text, opts = {}) {
  return new TextRun({
    text,
    font: "Georgia",
    size: opts.size || 21,
    color: opts.color || DARK,
    bold: opts.bold,
    italics: opts.italic,
  });
}

function p(runs, opts = {}) {
  const arr = Array.isArray(runs)
    ? runs
    : [typeof runs === "string" ? t(runs) : runs];
  return new Paragraph({
    children: arr,
    alignment: opts.align || AlignmentType.JUSTIFIED,
    spacing: { line: 320, after: opts.after !== undefined ? opts.after : 180 },
  });
}

function bullet(text) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    children: [t(text)],
    spacing: { line: 300, after: 100 },
  });
}

function sectionTitle(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: "Arial", size: 22, bold: true, color: RUST })],
    spacing: { before: 240, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RUST } },
  });
}

function rule(color = "DDDDDD") {
  return new Paragraph({
    children: [new TextRun("")],
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color } },
    spacing: { before: 0, after: 80 },
  });
}

// ── Header istituzionale (tabella 2 colonne) ──────────────────────────────────
const headerTable = new Table({
  width: { size: 9026, type: WidthType.DXA },
  columnWidths: [4800, 4226],
  borders: {
    top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
    left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
    insideH: { style: BorderStyle.NONE }, insideV: { style: BorderStyle.NONE },
  },
  rows: [new TableRow({
    children: [
      // Colonna sinistra — brand
      new TableCell({
        width: { size: 4800, type: WidthType.DXA },
        borders: {
          top: { style: BorderStyle.NONE }, left: { style: BorderStyle.NONE },
          right: { style: BorderStyle.NONE },
          bottom: { style: BorderStyle.SINGLE, size: 12, color: RUST },
        },
        margins: { top: 0, bottom: 160, left: 0, right: 200 },
        children: [
          new Paragraph({
            children: [new TextRun({ text: "ReMaker AI", bold: true, size: 44, color: RUST, font: "Arial" })],
            spacing: { after: 40 },
          }),
          new Paragraph({
            children: [new TextRun({ text: "Non buttare. Reinventa.", italics: true, size: 18, color: GRAY, font: "Arial" })],
            spacing: { after: 0 },
          }),
        ],
      }),
      // Colonna destra — mittente
      new TableCell({
        width: { size: 4226, type: WidthType.DXA },
        borders: {
          top: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
          left: { style: BorderStyle.NONE },
          bottom: { style: BorderStyle.SINGLE, size: 12, color: RUST },
        },
        margins: { top: 0, bottom: 160, left: 200, right: 0 },
        children: [
          new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 40 },
            children: [new TextRun({ text: "Roberto Faccenda", bold: true, size: 20, font: "Arial", color: DARK })] }),
          new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 20 },
            children: [new TextRun({ text: "CEO, INCAS Film srl", size: 17, font: "Arial", color: GRAY })] }),
          new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 20 },
            children: [new TextRun({ text: "Coordinatore Accademico", size: 17, font: "Arial", color: GRAY })] }),
          new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 20 },
            children: [new TextRun({ text: "Istituto Pantheon Design & Technology", size: 17, font: "Arial", color: GRAY })] }),
          new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 0 },
            children: [new TextRun({ text: "roberto.faccenda@istitutopantheon.it", size: 17, font: "Arial", color: RUST })] }),
        ],
      }),
    ],
  })],
});

// ── Riquadro oggetto ──────────────────────────────────────────────────────────
const oggettoBox = new Table({
  width: { size: 9026, type: WidthType.DXA },
  columnWidths: [9026],
  borders: {
    top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
    left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
    insideH: { style: BorderStyle.NONE }, insideV: { style: BorderStyle.NONE },
  },
  rows: [new TableRow({
    children: [new TableCell({
      width: { size: 9026, type: WidthType.DXA },
      borders: {
        top: { style: BorderStyle.SINGLE, size: 4, color: RUST },
        bottom: { style: BorderStyle.SINGLE, size: 4, color: RUST },
        left: { style: BorderStyle.SINGLE, size: 4, color: RUST },
        right: { style: BorderStyle.SINGLE, size: 4, color: RUST },
      },
      shading: { fill: LIGHT, type: ShadingType.CLEAR },
      margins: { top: 120, bottom: 120, left: 200, right: 200 },
      children: [new Paragraph({
        spacing: { after: 0 },
        children: [
          new TextRun({ text: "Oggetto: ", bold: true, size: 21, font: "Georgia", color: DARK }),
          new TextRun({ text: "Invito alla beta pilota di ReMaker AI — co-legitimazione istituzionale", size: 21, font: "Georgia", color: DARK }),
        ],
      })],
    })],
  })],
});

// ── Corpo lettera ─────────────────────────────────────────────────────────────
const corpo = [

  p("Gentile [Nome Referente],", { after: 280 }),

  p([
    t("Le scrivo in qualità di fondatore di "),
    t("ReMaker AI", { bold: true }),
    t(", un progetto italiano di innovazione sociale che ha l’obiettivo di dare una seconda vita agli oggetti inutilizzati attraverso l’intelligenza artificiale."),
  ]),

  p([
    t("ReMaker AI è oggi disponibile come bot Telegram ("),
    t("@ReMakerAI_bot", { bold: true }),
    t("): basta fotografare un oggetto per ricevere, in meno di quindici secondi, una stima del suo valore di mercato, cinque idee concrete di riuso, un annuncio pronto da pubblicare su piattaforme come Subito o eBay e indicazioni su dove donarlo o smaltirlo correttamente."),
  ]),

  p([
    t("Il progetto nasce da una convinzione precisa: la difficoltà di valorizzare gli oggetti che non usiamo più non è un problema tecnologico, è un problema di accesso alle informazioni. Milioni di persone ogni anno buttano oggetti che potrebbero essere venduti, donati o trasformati, semplicemente perché non sanno come farlo. ReMaker AI abbatte questa barriera."),
  ]),

  p([
    t("Il posizionamento del progetto è quello del "),
    t("welfare tech", { bold: true }),
    t(": uno strumento digitale con una missione sociale, pensato non solo per i consumatori più tecnologici, ma per chiunque voglia fare una scelta responsabile nei confronti degli oggetti e delle risorse."),
  ]),

  sp(120),
  sectionTitle("Perché scriviamo a [Nome Organizzazione]"),
  sp(60),

  p([
    t("[Nome Organizzazione] è tra le realtà che più coerentemente incarnano i valori attorno ai quali ReMaker AI è stato costruito: la riduzione degli sprechi, il supporto alle persone in difficoltà economica, la cultura del riuso come pratica quotidiana."),
  ]),

  p([
    t("Per questa ragione, ci piacerebbe "),
    t("coinvolgervi come partner della nostra beta pilota", { bold: true }),
    t(". Non si tratta di un accordo commerciale né di un impegno oneroso: vi chiediamo di testare lo strumento con la vostra rete, di restituirci un feedback strutturato e, se il progetto vi convincerà, di figurare tra i partner istituzionali che co-legitimano ReMaker AI nella sua fase di lancio pubblico."),
  ]),

  sp(120),
  sectionTitle("Cosa vi chiediamo — concretamente"),
  sp(60),

  bullet("Testare il bot @ReMakerAI_bot con un gruppo di volontari, operatori o beneficiari della vostra organizzazione per un periodo di 30 giorni."),
  bullet("Compilare un breve questionario di feedback (10 domande, circa 5 minuti) al termine del periodo di test."),
  bullet("Autorizzarci, se il progetto vi convincerà, a citare [Nome Organizzazione] tra i partner istituzionali della beta pilota nelle nostre comunicazioni pubbliche, nel pitch e nei materiali presentati a investitori e bandi."),

  sp(120),
  sectionTitle("Cosa offriamo in cambio"),
  sp(60),

  bullet("Accesso gratuito e prioritario alla versione definitiva di ReMaker AI per tutta la vostra organizzazione."),
  bullet("Co-authoring di un breve report pubblico sui risultati della beta pilota, utilizzabile nelle vostre comunicazioni istituzionali."),
  bullet("Visibilità come partner fondatore nel pitch agli investitori e nelle presentazioni istituzionali del progetto."),
  bullet("Una call di aggiornamento mensile durante la beta per condividere dati e orientare lo sviluppo futuro dello strumento."),

  sp(200),

  p([
    t("Può provare l'app direttamente dal browser all'indirizzo "),
    new ExternalHyperlink({
      link: "https://remaker-ai.roberto-faccenda.workers.dev/remaker-test",
      children: [new TextRun({ text: "remaker-ai.roberto-faccenda.workers.dev/remaker-test", font: "Georgia", size: 21, color: RUST, style: "Hyperlink" })],
    }),
    t(", oppure testare il bot Telegram cercando "),
    t("@ReMakerAI_bot", { bold: true }),
    t(". Sarò felice di organizzare una breve call di presentazione — venti minuti — per rispondere a qualsiasi domanda e illustrare nel dettaglio come potremmo strutturare la collaborazione."),
  ]),

  p("Rimango a disposizione e confido in un riscontro positivo.", { after: 400 }),

  // Firma
  p("Cordialmente,", { align: AlignmentType.LEFT, after: 320 }),
  new Paragraph({ children: [new TextRun({ text: "Roberto Faccenda", bold: true, size: 24, font: "Georgia", color: DARK })], spacing: { after: 60 } }),
  new Paragraph({ children: [new TextRun({ text: "CEO, INCAS Film srl", size: 18, font: "Georgia", color: GRAY })], spacing: { after: 40 } }),
  new Paragraph({ children: [new TextRun({ text: "Coordinatore Accademico, Istituto Pantheon Design & Technology", size: 18, font: "Georgia", color: GRAY })], spacing: { after: 40 } }),
  new Paragraph({ children: [new TextRun({ text: "roberto.faccenda@istitutopantheon.it", size: 18, font: "Georgia", color: RUST })], spacing: { after: 40 } }),
  new Paragraph({ children: [new TextRun({ text: "@ReMakerAI_bot  |  remaker-ai.roberto-faccenda.workers.dev/remaker-test", size: 17, font: "Georgia", color: GRAY, italics: true })], spacing: { after: 0 } }),

  sp(280),
  rule(RUST),
  sp(80),

  // Nota per il mittente
  new Paragraph({
    spacing: { after: 0 },
    children: [
      new TextRun({ text: "Nota per il mittente: ", bold: true, size: 17, font: "Georgia", color: GRAY }),
      new TextRun({ text: "Sostituire [Nome Referente], [Nome Organizzazione] e [DATA] con i dati reali. Personalizzare il paragrafo “Perché scriviamo a…” con un riferimento specifico al lavoro e ai valori dell’organizzazione destinataria.", size: 17, font: "Georgia", color: GRAY, italics: true }),
    ],
  }),
];

// ── Documento ─────────────────────────────────────────────────────────────────
const doc = new Document({
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "•",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } },
      }],
    }],
  },
  styles: {
    default: { document: { run: { font: "Georgia", size: 21, color: DARK } } },
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: { top: 1080, right: 1134, bottom: 1134, left: 1134 },
      },
    },
    children: [
      headerTable,
      sp(360),

      // Data (allineata a destra)
      new Paragraph({
        alignment: AlignmentType.RIGHT,
        spacing: { after: 360 },
        children: [new TextRun({ text: "Roma, [DATA]", size: 18, font: "Georgia", color: GRAY, italics: true })],
      }),

      // Destinatario
      new Paragraph({ children: [t("[Nome Referente]", { bold: true })], spacing: { after: 40 } }),
      new Paragraph({ children: [t("[Ruolo]")], spacing: { after: 40 } }),
      new Paragraph({ children: [t("[Nome Organizzazione]", { bold: true })], spacing: { after: 40 } }),
      new Paragraph({ children: [t("[Indirizzo]")], spacing: { after: 360 } }),

      oggettoBox,
      sp(320),

      ...corpo,
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/sessions/awesome-vigilant-galileo/mnt/remaker/remaker_lettera_partner.docx', buf);
  console.log('OK — lettera generata');
}).catch(e => { console.error(e); process.exit(1); });
