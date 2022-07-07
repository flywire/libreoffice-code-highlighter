CH2_STRINGS = {"en": { # dialog controls (label text + help text)
                      "label_lang": ("Language", ""),
                      "label_style": ("Style", ""),
                      "check_charstyles": ("Use character ~styles in Writer", "When possible, code highlighting is based on character styles."),
                      "check_col_bg": ("Set ~background color", "Use the background color provided by the style."),
                      "check_linenb": ("Add ~line numbering", "Active or deactivate line numbers."),
                      "nb_line": ("Line numbering", ""),
                      "cs_line": ("Character styles", ""),
                      "lbl_nb_start": ("Start at", ""),
                      "lbl_nb_ratio": ("Height (%)", ""),
                      "lbl_nb_sep": ("Separator", ""),
                      "lbl_styleprefix": ("Custom prefix:", "Leave empty to use internal style names."),
                      "nb_sep": ("", ""),
                      "pygments_ver": ("Build upon Pygments {}", ""),
                      "topage1": ("Back", ""),
                      "topage2": ("More...", ""),
                       # messages
                      "errlang": "Unsupported language.",
                      "errstyle": "Unknown style.",
                      "errsel1": "Unsupported selection.",
                      "errsel2": "Nothing to highlight.",
                      },

               "fr": { # contrôles de dilaogue (texte + texte d'aide)
                      "label_lang": ("Langage", ""),
                      "label_style": ("Style", ""),
                      "check_charstyles": ("Utiliser les ~styles de caractère dans Writer", "Si possible, le code ser colorisé sur base des styles de caractère."),
                      "check_col_bg": ("Utiliser la couleur de ~fond", "Utiliser l'arrière-plan fourni par le style."),
                      "check_linenb": ("Numéroter les ~lignes", "Affiche ou masque les numéros de ligne."),
                      "nb_line": ("Numéros de ligne", ""),
                      "cs_line": ("Styles de caractères", ""),
                      "lbl_nb_start": ("Démarrer à", ""),
                      "lbl_nb_ratio": ("Taille (%)", ""),
                      "lbl_nb_sep": ("Séparateur", ""),
                      "lbl_styleprefix": ("Préfixe personnalisé :", "Laisser vide pour utiliser les noms de style internes."),
                      "nb_sep": ("", ""),
                      "pygments_ver": ("Basé sur Pygments {}", ""),
                      "topage1": ("Retour", ""),
                      "topage2": ("Plus...", ""),
                       # messages
                      "errlang": "Langage non supporté.",
                      "errstyle": "Style inconnu.",
                      "errsel1": "Sélection invalide.",
                      "errsel2": "Rien à coloriser.",
                      }
               }


def getstrings(ctx):
    '''Get interface locale'''
    ps = ctx.ServiceManager.createInstanceWithContext("com.sun.star.util.PathSubstitution", ctx)
    vlang = ps.getSubstituteVariableValue("vlang")
    lang = vlang.split("-")[0]
    # print('vlang: {}'.format(vlang))
    # print('lang: {}'.format(lang))
    return CH2_STRINGS.get(lang, CH2_STRINGS["en"])
