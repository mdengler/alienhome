(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(TeX-PDF-mode t)
 '(TeX-output-view-style
   (quote
    (("^dvi$"
      ("^landscape$" "^pstricks$\\|^pst-\\|^psfrag$")
      "%(o?)dvips -t landscape %d -o && gv %f")
     ("^dvi$" "^pstricks$\\|^pst-\\|^psfrag$" "%(o?)dvips %d -o && gv %f")
     ("^dvi$" ("^a4\\(?:dutch\\|paper\\|wide\\)\\|sem-a4$" "^landscape$")
      "%(o?)xdvi %dS -paper a4r -s 0 %d")
     ("^dvi$" "^a4\\(?:dutch\\|paper\\|wide\\)\\|sem-a4$"
      "%(o?)xdvi %dS -paper a4 %d")
     ("^dvi$" ("^a5\\(?:comb\\|paper\\)$" "^landscape$")
      "%(o?)xdvi %dS -paper a5r -s 0 %d")
     ("^dvi$" "^a5\\(?:comb\\|paper\\)$" "%(o?)xdvi %dS -paper a5 %d")
     ("^dvi$" "^b5paper$" "%(o?)xdvi %dS -paper b5 %d")
     ("^dvi$" "^letterpaper$" "%(o?)xdvi %dS -paper us %d")
     ("^dvi$" "^legalpaper$" "%(o?)xdvi %dS -paper legal %d")
     ("^dvi$" "^executivepaper$" "%(o?)xdvi %dS -paper 7.25x10.5in %d")
     ("^dvi$" "." "%(o?)xdvi %dS %d") ("^pdf$" "" "evince %o")
     ("^pdf$" "." "xpdf -remote %s -raise %o %(outpage)")
     ("^html?$" "." "netscape %o"))))
 '(auto-coding-alist
   (quote
    (("\\.\\(arc\\|zip\\|lzh\\|lha\\|zoo\\|[jew]ar\\|xpi\\|rar\\|7z\\|ARC\\|ZIP\\|LZH\\|LHA\\|ZOO\\|[JEW]AR\\|XPI\\|RAR\\|7Z\\)\\'" . no-conversion-multibyte)
     ("\\.\\(exe\\|EXE\\)\\'" . no-conversion)
     ("\\.\\(sx[dmicw]\\|odt\\|tar\\|t[bg]z\\)\\'" . no-conversion)
     ("\\.\\(gz\\|Z\\|bz\\|bz2\\|xz\\|gpg\\)\\'" . no-conversion)
     ("\\.\\(jpe?g\\|png\\|gif\\|tiff?\\|p[bpgn]m\\)\\'" . no-conversion)
     ("\\.pdf\\'" . no-conversion)
     ("/#[^/]+#\\'" . emacs-mule)
     ("tasksched-.*\\.xml\\'" . utf-16le-with-signature-dos))))
 '(auto-compression-mode t nil (jka-compr))
 '(auto-save-file-name-transforms
   '(("\\`/[^/]*:\\([^/]*/\\)*\\([^/]*\\)\\'" "/var/tmp/\\2" t)))
 '(auto-save-interval 30)
 '(auto-save-timeout 10)
 '(backup-by-copying t)
 '(backup-by-copying-when-linked t)
 '(blank-chars (quote tabs))
 '(blank-display-mappings nil)
 '(blink-cursor-mode nil)
 '(c-default-style (quote ((awk-mode . "awk") (other . "gnu"))))
 '(calculator-bind-escape nil)
 '(case-fold-search t)
 '(cider-prefer-local-resources t)
 '(cider-repl-history-file \.cider_repl_hist)
 '(cider-repl-history-size 50000)
 '(column-number-mode t)
 '(compose-mail-user-agent-warnings nil)
 '(csv-align-max-width 80)
 '(current-language-environment "UTF-8")
 '(custom-enabled-themes (quote (tango-dark)))
 '(custom-safe-themes
   '("c2e1201bb538b68c0c1fdcf31771de3360263bd0e497d9ca8b7a32d5019f2fae"
     "33ea268218b70aa106ba51a85fe976bfae9cf6931b18ceaf57159c558bbcd1e6"
     "e6df46d5085fde0ad56a46ef69ebb388193080cc9819e2d6024c9c6e27388ba9"
     "67e998c3c23fe24ed0fb92b9de75011b92f35d3e89344157ae0d544d50a63a72"
     "8db4b03b9ae654d4a57804286eb3e332725c84d7cdab38463cb6b97d5762ad26"
     "40f6a7af0dfad67c0d4df2a1dd86175436d79fc69ea61614d668a635c2cd94ab" default))
 '(default-input-method "rfc1345")
 '(delete-auto-save-files nil)
 '(delete-old-versions t)
 '(delete-selection-mode t)
 '(describe-char-unidata-list
   '(name old-name general-category decomposition iso-10646-comment))
 '(desktop-save-mode t)
 '(display-time-day-and-date t)
 '(display-time-mode t)
 '(epa-file-cache-passphrase-for-symmetric-encryption t)
 '(epa-file-inhibit-auto-save nil)
 '(epg-debug t)
 '(epg-gpg-program "gpg2")
 '(epg-pinentry-mode 'loopback)
 '(fci-rule-color "gray14")
 '(file-precious-flag t)
 '(fill-column 79)
 '(font-lock-maximum-decoration t)
 '(font-lock-mode t t (font-lock))
 '(font-lock-use-colors t)
 '(font-lock-use-fonts nil)
 '(global-auto-revert-mode t)
 '(global-font-lock-mode t nil (font-lock))
 '(global-hl-line-mode t)
 '(global-linum-mode nil)
 '(gnus-carpal nil t)
 '(gnus-expert-user t)
 '(gnus-group-list-inactive-groups nil)
 '(gnus-inhibit-startup-message t)
 '(gnus-nntp-server nil)
 '(gnus-novice-user nil)
 '(gnus-secondary-select-methods
   '((nnimap "imap.gmail.com" (nnimap-server-port 993) (nnimap-stream ssl)
             (nnmail-expiry-wait immediate))
     (nnmaildir "local" (directory "~/.mail"))))
 '(gnus-select-method '(nneething "/home/martin/doc"))
 '(gnus-treat-display-xface (quote head) t)
 '(gnus-visual
   (quote (summary-highlight group-highlight article-highlight mouse-face summary-menu
                             group-menu article-menu tree-highlight menu highlight
                             browse-menu server-menu page-marker tree-menu
                             binary-menu pick-menu grouplens-menu)))
 '(gnutls-algorithm-priority "normal:-vers-tls1.3")
 '(graphviz-dot-auto-preview-on-save t)
 '(graphviz-dot-preview-extension "svg")
 '(graphviz-dot-revert-delay 3)
 '(graphviz-dot-view-command "dotty %s")
 '(highlight-symbol-idle-delay 0)
 '(highlight-symbol-only-when-region-active-p t)
 '(ido-mode 'buffer nil (ido))
 '(indent-tabs-mode nil)
 '(inferior-lisp-program "sbcl" t)
 '(inhibit-startup-echo-area-message "martin")
 '(inhibit-startup-screen t)
 '(initial-scratch-message nil)
 '(ispell-silently-savep t)
 '(iswitchb-mode t)
 '(kept-new-versions 5)
 '(kept-old-versions 5)
 '(load-home-init-file t t)
 '(lpr-command "lpr")
 '(lpr-switches
   (quote ("-o media=letter" "-o raw" "-o sides=two-sided-long-edge" "-o print-quality=5")))
 '(mail-envelope-from (quote header))
 '(mail-mode-hook (quote (flyspell-mode mail-abbrevs-setup)))
 '(mail-self-blind t)
 '(mail-specify-envelope-from t)
 '(markdown-command "pandoc --standalone")
 '(markdown-display-remote-images t)
 '(markdown-enable-math t)
 '(markdown-enable-wiki-links t)
 '(markdown-use-pandoc-style-yaml-metadata t)
 '(menu-bar-mode nil)
 '(message-citation-line-format "On %a, %b %d %Y at %r, %f wrote:")
 '(message-citation-line-function (quote message-insert-formatted-citation-line))
 '(message-fcc-externalize-attachments t)
 '(message-mode-hook (quote (flyspell-mode mail-abbrevs-setup)))
 '(message-send-mail-function (quote message-send-mail-with-sendmail))
 '(message-sendmail-envelope-from (quote header))
 '(message-sendmail-f-is-evil t)
 '(message-user-fqdn "martindengler.com")
 '(mu4e-compose-signature-auto-include nil)
 '(mu4e-drafts-folder "/Drafts")
 '(mu4e-headers-date-format "%y-%m-%d %H:%M")
 '(mu4e-headers-fields '((:flags . 3) (:date . 16) (:from . 14) (:subject)))
 '(mu4e-headers-leave-behavior 'apply)
 '(mu4e-headers-results-limit 1000)
 '(mu4e-headers-skip-duplicates t)
 '(mu4e-headers-visible-lines 20)
 '(mu4e-html2text-command
   "elinks -dump -dump-charset iso-8859-15 -default-mime-type text/html")
 '(mu4e-maildir-shortcuts nil)
 '(mu4e-mu-binary "/home/martin/bin/mu")
 '(mu4e-my-email-addresses
   '("martin@martindengler.com" "mdengler@gmail.com"
     "martin.dengler@decuragroup.com" "mtd@sugarlabs.org" "mtd@ieee.org"
     "Martin.T.Dengler.97@dartmouth.edu" "nosp@xades.com" "martin@xades.com"
     "martin@iai.com.hk" "martin@martin.hk" "martin@xades.hk"
     "martin@denglers.com" "root@martindengler.com"))
 '(mu4e-refile-folder "/archive")
 '(mu4e-search-results-limit 1000)
 '(mu4e-search-skip-duplicates t)
 '(mu4e-sent-folder "/Sent")
 '(mu4e-show-images t)
 '(mu4e-trash-folder "/Trash")
 '(mu4e-update-interval 240)
 '(mu4e-use-fancy-chars t)
 '(mu4e-user-mail-address-list
   '("martin@martindengler.com" "mdengler@gmail.com"
     "martin.dengler@decuragroup.com" "mtd@sugarlabs.org" "mtd@ieee.org"
     "Martin.T.Dengler.97@dartmouth.edu" "nosp@xades.com" "martin@xades.com"
     "martin@iai.com.hk" "martin@martin.hk" "martin@xades.hk"
     "martin@denglers.com" "root@martindengler.com"))
 '(mu4e-view-date-format "%y-%m-%d %H:%M")
 '(mu4e-view-show-addresses t)
 '(mu4e-view-show-images t)
 '(next-line-add-newlines nil)
 '(nrepl-message-colors
   (quote
    ("#CC9393" "#DFAF8F" "#F0DFAF" "#7F9F7F" "#BFEBBF" "#93E0E3" "#94BFF3" "#DC8CC3")))
 '(org-babel-load-languages (quote ((emacs-lisp . t) (dot . t))))
 '(package-archives
   '(("melpa-stable" . "https://melpa.org/packages/")
     ("gnu" . "https://elpa.gnu.org/packages/")))
 '(package-selected-packages
   '(## anti-zenburn-theme apheleia auto-complete-exuberant-ctags bbdb blacken
        cl-lib cl-lib-highlight cl-libify cl-print clojure-mode
        color-theme-solarized color-theme-zenburn csv csv-mode d2-mode dad-joke
        deft doneburn-theme dot-mode editorconfig ellama flycheck
        flycheck-color-mode-line flycheck-pycheckers git-gutter+
        git-gutter-fringe+ gitlab-ci-mode gitlab-ci-mode-flycheck
        gitlab-pipeline gnuplot gptel graphviz-dot-mode highlight-symbol
        impatient-mode magit-annex magit-gitflow magit-gptcommit
        magit-org-todos magit-todos magit-tramp markdown-mode markdown-mode+
        markdown-preview-eww markdown-preview-mode mu-cite mu4e
        mu4e-maildirs-extension mu4e-overview mu4e-views ox-pandoc ox-tufte
        pandoc-mode pet python-black shr skewer-mode unicode-fonts
        url-http-oauth w3m zeitgeist zenburn zenburn-theme))
 '(paren-mode (quote sexp) nil (paren))
 '(pr-ps-printer-alist (quote ((default "lpr" nil "-P" ""))))
 '(pr-txt-printer-alist (quote ((default "lpr" nil ""))))
 '(ps-paper-type (quote a4))
 '(ps-paper-type (quote letter))
 '(ps-printer-name nil)
 '(python-shell-interpreter "uv")
 '(python-shell-interpreter-args "run python -i")
 '(rcirc-server-alist
   (quote
    (("irc.freenode.net" :channels
      ("#rcirc" "#bash" "#clojure" "#python")
      :encryption tls))))
 '(remember-mailbox "~/Maildir/todo")
 '(remote-shell-program "ssh")
 '(safe-local-variable-values
   (quote
    ((coding-system . utf-8)
     (encoding . utf-8)
     (eval add-hook 'before-save-hook #'python-black-buffer nil t)
     (eval add-hook 'before-save-hook #'clang-format-buffer nil t)
     (package-lint-main-file . "llm.el")
     (rpm-change-log-uses-utc . t)
     (rpm-change-log-uses-utc . t))))
 '(save-place-mode t nil (saveplace))
 '(save-place-skip-check-regexp
   "\\`/\\(?:cdrom\\|floppy\\|mnt\\|\\(?:[^@/:]*@\\)?[^@/:]*[^@/:.]:\\)")
 '(scroll-bar-mode nil)
 '(send-mail-function (quote smtpmail-send-it))
 '(sendmail-program (expand-file-name "~/bin/msmtpq"))
 '(shell-completion-fignore (quote ("~" "#" "%")))
 '(shell-mode-hook (quote (ansi-color-for-comint-mode-on)))
 '(show-paren-mode t nil (paren))
 '(show-paren-style (quote expression))
 '(show-trailing-whitespace t)
 '(size-indication-mode t)
 '(smooth-scroll-margin 3)
 '(smtpmail-debug-info t)
 '(smtpmail-smtp-server "mail.xades.com")
 '(smtpmail-smtp-service 587)
 '(smtpmail-stream-type (quote starttls))
 '(speedbar-default-position (quote right))
 '(speedbar-track-mouse-flag t)
 '(speedbar-use-images nil)
 '(speedbar-verbosity-level 2)
 '(tab-width 4)
 '(text-mode-hook '(auto-fill-mode text-mode-hook-identify))
 '(tool-bar-mode nil)
 '(transient-mark-mode t)
 '(truncate-lines nil)
 '(user-full-name "Martin T Dengler")
 '(user-mail-address "martin@martindengler.com")
 '(vc-annotate-background "#3b3b3b")
 '(vc-annotate-color-map
   (quote
    ((20 . "#dd5542")
     (40 . "#CC5542")
     (60 . "#fb8512")
     (80 . "#baba36")
     (100 . "#bdbc61")
     (120 . "#7d7c61")
     (140 . "#6abd50")
     (160 . "#6aaf50")
     (180 . "#6aa350")
     (200 . "#6a9550")
     (220 . "#6a8550")
     (240 . "#6a7550")
     (260 . "#9b55c3")
     (280 . "#6CA0A3")
     (300 . "#528fd1")
     (320 . "#5180b3")
     (340 . "#6380b3")
     (360 . "#DC8CC3"))))
 '(vc-annotate-very-old-color "#DC8CC3" t)
 '(w3m-use-cookies t)
 '(warning-suppress-types '((comp)))
 '(winner-mode t nil (winner))
 '(zen-encumbered-urls
   (quote
    ("#brief timewastes" "www.penny-arcade.com" "www.dilbert.com" "www.xkcd.com" "www.userfriendly.org" "#news waste" "slashdot.org" "dn.se" "#social timewastes" "https://www.facebook.com")))
 '(zen-fullscreen-mode t))

(put 'downcase-region 'disabled nil)
(put 'narrow-to-region 'disabled nil)

(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(blank-tab-face ((((class mono)) :inverse-video t) (t (:background "Red" :foreground "White"))))
 '(font-lock-doc-string-face ((((class color) (background light)) (:foreground "orange"))))
 '(font-lock-string-face ((((class color) (background light)) (:foreground "darkgreen"))))
 '(highlight-symbol-face ((t (:background "sienna"))))
 '(markdown-header-face ((t (:inherit font-lock-function-name-face :weight bold))))
 '(markdown-header-face-1 ((t (:inherit font-lock-keyword-face :height 1.0))))
 '(markdown-header-face-2 ((t (:inherit font-lock-type-face :height 1.0))))
 '(markdown-header-face-3 ((t (:inherit font-lock-variable-name-face :height 1.0))))
 '(rst-level-1 ((t (:background "green"))))
 '(show-paren-match ((((class color) (background light)) (:background "green"))))
 '(trailing-whitespace ((((class color) (background light)) (:background "lightyellow")))))

;; If running under screen, disable C-z.
;; from http://www4.informatik.uni-erlangen.de/~jnweiger/screen-faq.html
;; ...and correct backspace/delete problem
;; from http://www.gnu.org/software/emacs/manual/html_node/emacs/DEL-Does-Not-Delete.html
(when (not window-system)
  (when (equal (getenv "TERM") "cygwin")
    (message "running in cygwin/not putty, so correcting backspace/delete")
    (normal-erase-is-backspace-mode 1))
  (when (getenv "STY")
    (message "running in screen, so disabling C-z")
    (global-unset-key "\C-z")
    (unless (key-binding [(delete)])
      (global-set-key [(delete)] "\C-d"))))

;; cycle buffers with C-Tab, ignoring uninteresting ones
;; ripped from http://www.cubic.org/~doj/emacs, which...
;; ripped from http://www.dotemacs.de/dotfiles/KilianAFoth.emacs.html
(defun backward-buffer () (interactive)
  "Switch to previously selected buffer."
  (let* ((list (cdr (buffer-list)))
         (buffer (car list)))
    (while (and (cdr list) (string-match "\\*" (buffer-name buffer)))
      (progn
        (setq list (cdr list))
        (setq buffer (car list))))
    (bury-buffer)
    (switch-to-buffer buffer)))

(defun forward-buffer () (interactive)
  "Opposite of backward-buffer."
  (let* ((list (reverse (buffer-list)))
         (buffer (car list)))
    (while (and (cdr list) (string-match "\\*" (buffer-name buffer)))
      (progn
        (setq list (cdr list))
        (setq buffer (car list))))
    (switch-to-buffer buffer)))

(global-set-key [(control tab)] 'backward-buffer)
(global-set-key [(control shift kp-tab)] 'forward-buffer)
(global-set-key [(control shift iso-lefttab)] 'forward-buffer)
(global-set-key [(control shift iso-righttab)] 'forward-buffer)
;; end rip


;; Make all yes/no prompts into y/n prompts
(fset 'yes-or-no-p 'y-or-n-p)

;; sort-region-with-shell
(fset 'sort-region-with-shell
      [?\C-u ?1 escape ?| ?s ?o ?r ?t return])

(setq calculator-user-operators
      '(("tf" cl-to-fr (+ 32 (/ (* X 9) 5)) 1)
        ("tc" fr-to-cl (/ (* (- X 32) 5) 9) 1)
        ("tp" kg-to-lb (/ X 0.453592)       1)
        ("tk" lb-to-kg (* X 0.453592)       1)
        ("tF" mt-to-ft (/ X 0.3048)         1)
        ("tM" ft-to-mt (* X 0.3048)         1)))

;; from http://www.cubic.org/~doj/emacs
;; set time to show in corner
(display-time)

(put 'scroll-left 'disabled nil)

;; from http://www.emacswiki.org/cgi-bin/emacs-en/McMahanEmacsConfiguration
(autoload 'ansi-color-for-comint-mode-on "ansi-color" nil t)


;; ;; run a few shells.
;; (shell "*shell5*")
;; (shell "*shell6*")
;; (shell "*shell7*")

;; ;; C-5, 6, 7 to switch to shells
;; (global-set-key [(control 5)]
;;                 (lambda () (interactive) (switch-to-buffer "*shell5*")))
;; (global-set-key [(control 6)]
;;                 (lambda () (interactive) (switch-to-buffer "*shell6*")))
;; (global-set-key [(control 7)]
;;                 (lambda () (interactive) (switch-to-buffer "*shell7*")))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Emacs 24 package management
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; package.el is at http://repo.or.cz/w/emacs.git/blob_plain/1a0a666f941c99882093d7bd08ced15033bc3f0c:/lisp/emacs-lisp/package.el


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Compile .emacs, and recompile if .emacs is newer
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(when (and user-init-file
           (equal (file-name-extension user-init-file) "elc"))
  (let* ((source (file-name-sans-extension user-init-file))
         (alt (concat source ".el")))
    (setq source (cond ((file-exists-p alt) alt)
                       ((file-exists-p source) source)
                       (t nil)))
    (when source
      (when (file-newer-than-file-p source user-init-file)
        (byte-compile-file source)
        (load-file source)
        (eval-buffer nil nil)
        (delete-other-windows) ))))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Library loading
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(let ((default-directory (concat user-emacs-directory
                                 (convert-standard-filename "site-lisp/"))))
  (normal-top-level-add-to-load-path '("."))
  (normal-top-level-add-subdirs-to-load-path))


(setq with-library-load-libraries
      (or (getenv "EMACS_LOAD_LIBS")
          (getenv "EMACS_LOAD_LIBRARIES")))
; (setenv "EMACS_LOAD_LIBS" "1")

;; from http://www.emacswiki.org/cgi-bin/emacs-en/LoadingLispFiles
(defmacro with-library (symbol &rest body)
  `(condition-case err-desc
       (when with-library-load-libraries
         (message (format "Loading %s ..." ',symbol))
         (require ',symbol)
         (message         "              ...OK")
         ,@body)
     (error (message (format "Loading %s ...failed: %s" ',symbol err-desc))
            nil)))
(put 'with-library 'lisp-indent-function 1)


(with-library anything ())
(with-library anything-config ())

(with-library auto-complete
  (global-auto-complete-mode t)

  (with-library auto-complete-yasnippet)
  (with-library auto-complete-python)
  (with-library ac-python)
  (with-library auto-complete-css)
  (with-library auto-complete-cpp)
  (with-library auto-complete-emacs-lisp)
  (with-library auto-complete-semantic)
  (with-library auto-complete-gtags)

  (global-auto-complete-mode t)
  (setq ac-auto-start 3)
  (setq ac-dwim t)
  (set-default 'ac-sources '(ac-source-yasnippet ac-source-abbrev ac-source-words-in-buffer ac-source-files-in-current-dir ac-source-symbols))
    )


;; from http://emacs-fu.blogspot.com/2009/08/managing-e-mail-addresses-with-bbdb.html
(setq bbdb-file "~/.emacs.d/bbdb") ;; keep ~/ clean; set before loading
(with-library bbdb
  (bbdb-initialize)
  (setq
   bbdb-offer-save 1        ;; 1 means save-without-asking
   bbdb-use-pop-up t        ;; allow popups for addresses
   bbdb-electric-p t        ;; be disposable with SPC
   bbdb-popup-target-lines  1             ;; very small
   bbdb-dwim-net-address-allow-redundancy t ;; always use full name
   bbdb-quiet-about-name-mismatches 2 ;; show name-mismatches 2 secs
   bbdb-always-add-address t ;; add new addresses to existing...
   ;; ...contacts automatically
   bbdb-canonicalize-redundant-nets-p t ;; x@foo.bar.cx => x@bar.cx
   bbdb-completion-type nil             ;; complete on anything
   bbdb-complete-name-allow-cycling t   ;; cycle through matches
   ;; this only works partially
   bbbd-message-caching-enabled t ;; be fast
   bbdb-use-alternate-names t     ;; use AKA
   bbdb-elided-display t          ;; single-line addresses
   ;; auto-create addresses from mail
   bbdb/mail-auto-create-p 'bbdb-ignore-some-messages-hook
   bbdb-ignore-some-messages-alist ;; don't ask about fake addresses
   ;; NOTE: there can be only one entry per header (such as To, From)
   ;; http://flex.ee.uec.ac.jp/texi/bbdb/bbdb_11.html
   '(( "From" . "no.?reply\\|DAEMON\\|daemon\\|facebookmail\\|twitter")))
  )


(with-library blank-mode ())

;; from http://emacs-fu.blogspot.com/2009/01/e-mail-with-emacs-using-mutt.html
(with-library cl-lib
  (with-library post
    (add-hook 'mail-mode-hook 'post-mode)))

;(setq mail-mode-hook nil)

(with-library clojure-mode
  (with-library cider
    (add-hook 'cider-mode-hook 'cider-turn-on-eldoc-mode 'subword-mode 'smartparens-strict-mode)))

;; (with-library color-theme
;;   (with-library zenburn (color-theme-zenburn))
;;   (with-library tango-2 ())
;;   (with-library tango-2-theme ())
;;   (with-library tango-plus-theme ())
;;   (with-library tango-tango-theme ())
;;   (with-library zenburn-theme ())
;;   (with-library zerodark-theme ())
;;   )

(with-library cosmetic ())

;; desktop mode lets us saves buffer state. activate it with M-x desktop-save RET.
(with-library desktop (desktop-save-mode 1))

;(with-library dev-p4 ())

(with-library dircolors ())

(with-library edit-server
  (edit-server-start))

(with-library editorconfig
  (editorconfig-mode 1))

(with-library epa-file
  (epa-file-enable))

(with-library fill-column-indicator
  (add-hook 'python-mode-hook 'fci-mode))

; http://emacs.1067599.n8.nabble.com/Emacs-as-an-external-flowed-text-editor-td60049.html
(with-library flow-fill
  (defun mtd-fill-flowed ()
    "Call fill-flowed in flow-fill.el."
    (interactive)
    (fill-flowed)))

(with-library flycheck
  (add-hook 'python-mode-hook 'flycheck-mode))

(with-library magit
      (with-library git-gutter+
        (global-set-key "\C-xC" 'git-gutter+-stage-and-commit)
        (add-hook 'conf-mode-hook 'git-gutter+-mode)
        (add-hook 'conf-toml-mode-hook 'git-gutter+-mode)
        (add-hook 'python-mode-hook 'git-gutter+-mode)))

;(with-library git-gutter-fringe+
;  (add-hook 'python-mode-hook 'git-gutter-fringe+-mode))

(with-library graphviz-dot-mode ())

(with-library highlight ())

(with-library highlight-symbol
  (add-hook 'python-mode-hook highlight-symbol-mode))

(with-library hippie-exp
  (global-set-key "\M-/" 'hippie-expand))

(with-library htmlize ())

;; (with-library iswitchb
;;   (iswitchb-mode)
;;   (global-set-key "\C-xb" 'iswitchb-buffer))

(with-library ido-mode ())

(with-library linum ())

(with-library markdown-mode
    (add-to-list 'auto-mode-alist '("todo$" . markdown-mode))
    (add-to-list 'auto-mode-alist '(".plan$" . markdown-mode))
    (add-to-list 'auto-mode-alist '(".project$" . markdown-mode))
    (add-to-list 'auto-mode-alist '("\\.md$" . markdown-mode))
    (add-to-list 'auto-mode-alist '("\\.rst$" . markdown-mode))
    (add-to-list 'auto-mode-alist '("\\.txt$" . markdown-mode)))
(with-library markdown-mode+ ())

(with-library mu4e

  ;; from https://github.com/djcb/mu/issues/569
  (add-hook 'mu4e-compose-mode-hook
            (defun cpb-compose-setup ()
              "Use hard newlines, so outgoing mails will have format=flowed."
              (use-hard-newlines t 'guess)))

  ;; (require 'mu4e-maildirs-extension)
  (mu4e-maildirs-extension))

(with-library octave
  (add-to-list 'auto-mode-alist '("\\.m$" . octave-mode)))

(with-library org ())

(with-library package
  ;; list is in customize from emacs-26
  ;; (add-to-list 'package-archives
  ;;              '("marmalade" . "http://marmalade-repo.org/packages/"))
  ;; (add-to-list 'package-archives
  ;;              '("melpa" . "http://stable.melpa.org/packages/"))
  (package-initialize))

(with-library parenface ())

(with-library paredit ())

(with-library pymacs
;(setq auto-mode-alist (cons '("\\.py$" . python-mode) auto-mode-alist))
  (setq interpreter-mode-alist(cons '("python" . python-mode) interpreter-mode-alist))
;(setq py-python-command "python3")
;(autoload 'python-mode "python-mode" "Python editing mode." t)

;; pymacs settings
;(setq pymacs-python-command py-python-command)
  (autoload 'pymacs-load "pymacs" nil t)
  (autoload 'pymacs-eval "pymacs" nil t)
  (autoload 'pymacs-apply "pymacs")
  (autoload 'pymacs-call "pymacs")

  (with-library pycomplete)
  )

(with-library R
  (add-to-list 'auto-mode-alist '("\\.R$" . R-mode)))

(with-library rainbow-delimiters
  (rainbow-delimiters-mode)
  (add-hook 'lisp-mode-hook (lambda () (rainbow-delimiters-mode t)))
  (add-hook 'emacs-lisp-mode-hook (lambda () (rainbow-delimiters-mode t)))
  (add-hook 'clojure-mode-hook (lambda () (rainbow-delimiters-mode t)))
; rainbow-delimiters-mode is too slow for python in edge's emacs
;  (add-hook 'python-mode-hook (lambda () (rainbow-delimiters-mode t)))
  (add-hook 'REPL-mode-hook (lambda () (rainbow-delimiters-mode t)))
  )

(with-library rainbow-parens (rainbow-paren-mode))

(with-library readline-complete ())

(with-library scala-mode
  (require 'scala-mode-auto)
  (add-hook 'scala-mode-hook '(lambda () (scala-mode-feature-electric-mode)))
  (add-to-list 'auto-mode-alist '("\\.scala$" . scala-mode)))

(with-library ensime
  (add-hook 'scala-mode-hook 'ensime-scala-mode-hook))

(with-library server (server-start))

(with-library shebang ())

;; from http://bc.tech.coop/blog/040306.html
(with-library slime
  (require 'slime)
  (add-hook 'lisp-mode-hook (lambda () (slime-mode t)))
  (add-hook 'inferior-lisp-mode-hook (lambda () (inferior-slime-mode t)))
  ;; If you don't want eldoc-like behavior, comment out the following line
  ;;(slime-autodoc-mode)

  ;; from IRC
  (define-key slime-mode-map [tab] 'slime-indent-and-complete-symbol)

  ;; GNU CLISP - http://clisp.cons.org/
  (defun clisp-start ()
    (interactive)
    (shell-command (concat "/usr/bin/clisp -K full "
                           "-B /usr/lib64/clisp "
                           "-ansi -q -q&")))

  (slime-setup))

(with-library smartparens ())

(with-library smooth-scrolling ())

;; (with-library svg-mode-line-themes
;;   (smt/enable)
;;   (smt/set-theme 'diesel)
;;   (set-face-attribute 'mode-line nil :box nil)
;;   (set-face-attribute 'mode-line-inactive nil :box nil))

(with-library tracker-dired
  (global-set-key "\C-xt" 'tracker-dired))

(with-library tramp ())

(with-library w3m ())
(with-library w3m-session ())
(with-library w3m-cookie ())

(with-library windmove ())

(with-library zeitgeist ())

(with-library smartparens ())

(with-library svg-mode-line-themes
  (smt/enable)
  (smt/set-theme 'diesel)
  (set-face-attribute 'mode-line nil :box nil)
  (set-face-attribute 'mode-line-inactive nil :box nil))

;; probably should be the last library loaded
(with-library ffap (ffap-bindings))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Hooks & key bindings (mine, so last)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(global-set-key [(select)] 'end-of-line)
(global-set-key [(control select)] 'end-of-buffer)

;;C-next/prior (PgDn/PgUp) goes to next/prev interesting code block per interesting modes
;; we could remap backward/forward paragraph, but that's just different enough...
(global-set-key [(control shift next)] 'scroll-left)
(global-set-key [(control shift prior)] 'scroll-right)
(global-set-key [(control next)] 'forward-sexp)   ; useful surprisingly broadly
(global-set-key [(control prior)] 'backward-sexp)
;; (add-hook 'lisp-mode-hook
;;           '(lambda ()
;;              (local-set-key [(control next)] 'forward-sexp)
;;              (local-set-key [(control prior)] 'backward-sexp)))
;; (setq lisp-mode-hook ())

(add-hook 'REPL-mode-hook
           '(lambda ()
              (local-set-key [(control up)] 'slime-repl-previous-input)
              (local-set-key [(control down)] 'slime-repl-next-input)))
;; (setq REPL-mode-hook ())

(add-hook 'inferior-python-mode-hook
          '(lambda ()
             (local-set-key [(control n)] 'py-next-statement)
             (local-set-key [(control p)] 'py-previous-statement)
             (local-set-key [(control next)] 'py-next-statement)
             (local-set-key [(control prior)] 'py-previous-statement)
             (local-set-key [(meta n)] 'comint-next-matching-input-from-input)
             (local-set-key [(meta p)] 'comint-previous-matching-input-from-input)
             (local-set-key [(meta next)] 'comint-next-matching-input-from-input)
             (local-set-key [(meta prior)] 'comint-previous-matching-input-from-input)))
;; (setq inferior-python-mode-hook ())

(add-hook 'python-mode-hook
          '(lambda ()
             (local-set-key [(control next)] 'py-next-statement)
             (local-set-key [(control prior)] 'py-previous-statement)))
;; (setq python-mode-hook ())


(add-hook 'comint-mode-hook
          '(lambda ()
             (local-set-key [(control next)] 'comint-next-matching-input-from-input)
             (local-set-key [(control prior)] 'comint-previous-matching-input-from-input)))
;; (setq comint-mode-hook ())



;; S-insert pastes from the clipboard
;; C-insert copies to the clipboard
;; C-S-insert cuts to the clipboard
(global-set-key [(shift insert)] 'clipboard-yank)
(global-set-key [(control insert)] 'clipboard-kill-ring-save)
(global-set-key [(control shift insert)] 'clipboard-kill-region)

(global-set-key "\C-x\C-c" (lambda ()
                             (interactive)
                             (when (yes-or-no-p "Exit emacs? ") (save-buffers-kill-emacs))))


;; from http://www.vinc17.org/mutt/index.en.html
(defun mtd-mutt-ff-hook ()
  ;; mutt buffer name example: "/tmp/mutt-sun-617-6486"
  ;(message (format "mtd-mutt-ff-hook: buffer-file-name is %s" (buffer-file-name)))
  (when (string-match "mutt-.*\\(-[a-z0-9]+\\)+"
                      (file-name-nondirectory (buffer-file-name)))
    (set (make-local-variable 'backup-inhibited) t)
    (message (format "mtd-mutt-ff-hook: fill-column is %s." fill-column))
    ;; The following code is executed only when composing messages
    ;; (new messages or replies), not when editing messages (which
    ;; start with "From ") from the mailbox.
    (when (looking-at "^From:")
      (flush-lines "^\\(> \n\\)*> -- \\(\\(\n> .*\\)+\\|$\\)")
      (not-modified)
      (message (format "mtd-mutt-ff-hook: point is %s" (point)))
      (search-forward "\n\n" nil t)
      (message (format "mtd-mutt-ff-hook: point is %s" (point)))
      )
    (mail-mode)
    ;(enriched-mode)
    (setq fill-column (point-max))
    (message (format "mtd-mutt-ff-hook: ENDING fill-column is %s." fill-column))
    ))
;; (remove-hook 'find-file-hook 'mtd-mutt-ff-hook)
(add-hook 'find-file-hook 'mtd-mutt-ff-hook)
(add-to-list 'auto-mode-alist '("mutt-" . mtd-mutt-ff-hook))
;;(setq auto-mode-alist (delete '("/mutt-" . mtd-mutt-ff-hook) auto-mode-alist))
;;(setq auto-mode-alist (delete '("mutt-" . mtd-mutt-ff-hook) auto-mode-alist))
;;(add-to-list 'auto-mode-alist '("mutt-" . mtd-mutt-ff-hook))




;; from http://steve.yegge.googlepages.com/effective-emacs

(global-set-key "\C-x\C-m" 'execute-extended-command)
(global-set-key "\C-c\C-m" 'execute-extended-command)

;;(global-set-key "\C-w" 'backward-kill-word)
(global-set-key "\C-x\C-k" 'kill-region) ; we lose edit-kbd-macro, but so what
(global-set-key "\C-c\C-k" 'kill-region)

;; from me!
(global-set-key "\C-s" 'isearch-forward-regexp)
(defun mtd-invoke-isearch-with-symbol-near-point ()
  (interactive)
  (let ((search-string (thing-at-point 'symbol))
        (search-string-start (first (bounds-of-thing-at-point 'symbol))))
    (unless (eq search-string-start (point))
      (goto-char search-string-start))
    (isearch-resume search-string    ; SEARCH
                    t                ; REGEXP
                    nil              ; WORD
                    t                ; FORWARD
                    search-string    ; MESSAGE
                    t                ; CASE-FOLD
                    )
    (isearch-push-state)
    (isearch-update)
    ))
(global-set-key "\M-s" 'mtd-invoke-isearch-with-symbol-near-point)
(define-key isearch-mode-map "\M-s" 'isearch-repeat-forward)


; from http://stackoverflow.com/questions/43765/pin-emacs-buffers-to-windows-for-cscope
;; Toggle window dedication
(defun toggle-window-dedicated ()
  "Toggle whether the current active window is dedicated or not"
  (interactive)
  (message
   (if (let (window (get-buffer-window (current-buffer)))
         (set-window-dedicated-p window
                                 (not (window-dedicated-p window))))
       "Window '%s' is dedicated"
     "Window '%s' is normal")
   (current-buffer)))

(global-set-key [pause] 'toggle-window-dedicated)


(defun mtd-align-defun-to-top-of-viewable-screen ()
  ; doesn't do what I want right now
  (interactive)
  (narrow-to-defun)
  (widen))

(defun mtd-indent-after-comma-space ()
  (interactive)
  (re-search-forward ",[ ]+" (line-end-position) t)
  (replace-match ",")
  (newline-and-indent) ; consider reindent-then-newline-and-indent
  )
;(global-set-key "\C-," 'mtd-indent-after-comma-space)
(global-set-key (kbd "C-,") 'mtd-indent-after-comma-space)
;(global-set-key [(control ?.)] 'complete-symbol)
;(global-set-key (kbd "C-x K") 'kill-other-buffers-of-this-file-name)

(defun mtd-make-title-from-line (line)
  (progn
    (replace-regexp-in-string
     "[^-_a-zA-z0-9.]"
     ""
     (replace-regexp-in-string
      "_+"
      "_"
      (replace-regexp-in-string
       "[ :;/,#]"
       "_" line)))))

(defun mtd-save-current-buffer-as-journal-entry-file ()
  (interactive)
  (let* ((end-of-first-line (1+ (string-match "\n" (buffer-string))))
         (title-from-buffer (mtd-make-title-from-line
                             (buffer-substring-no-properties 1 end-of-first-line)))
         (timestamp (format-time-string "%Y%m%d-%H%M%S"))
         (filename
          (or buffer-file-name
              (expand-file-name
               (format "~/journal/%s_%s_%s.txt" timestamp (system-name) title-from-buffer)))))
    (progn
      (message filename)
      (set-visited-file-name filename)
      (save-buffer))))
(global-set-key "\M-j" 'mtd-save-current-buffer-as-journal-entry-file)


;; org-mode
(global-set-key "\C-cl" 'org-store-link)
(global-set-key "\C-cc" 'org-capture)
(global-set-key "\C-ca" 'org-agenda)
(global-set-key "\C-cb" 'org-iswitchb)




;;
;; from http://stackoverflow.com/questions/805050/eclipse-indentation-on-emacs
;;
;; eclipse-java-style is the same as the "java" style (copied from
;; cc-styles.el) with the addition of (arglist-cont-nonempty . ++) to
;; c-offsets-alist to make it more like default Eclipse formatting -- function
;; arguments starting on a new line are indented by 8 characters
;; (++ = 2 x normal offset) rather than lined up with the arguments on the
;; previous line
(defconst eclipse-java-style
  '((c-basic-offset . 4)
    (c-comment-only-line-offset . (0 . 0))
    ;; the following preserves Javadoc starter lines
    (c-offsets-alist . ((inline-open . 0)
                        (topmost-intro-cont    . +)
                        (statement-block-intro . +)
                        (knr-argdecl-intro     . 5)
                        (substatement-open     . +)
                        (substatement-label    . +)
                        (label                 . +)
                        (statement-case-open   . +)
                        (statement-cont        . +)
                        (arglist-intro  . c-lineup-arglist-intro-after-paren)
                        (arglist-close  . c-lineup-arglist)
                        (access-label   . 0)
                        (inher-cont     . c-lineup-java-inher)
                        (func-decl-cont . c-lineup-java-throws)
                        (arglist-cont-nonempty . ++)
                        )))
  "Eclipse Java Programming Style")
(c-add-style "ECLIPSE" eclipse-java-style)
(customize-set-variable 'c-default-style
                        (quote ((awk-mode . "awk")
                                ; (java-mode . "eclipse")
                                (other . "gnu"))))



;;
;; misc
;;


;; from https://github.com/brentonashworth/one/wiki/Emacs
;; Allow input to be sent to somewhere other than inferior-lisp


(setq shell-buffer-name "*shell*")

(defun shell-send-input (input)
  "Send INPUT into the *shell* buffer and leave it visible."
  (save-selected-window
    (switch-to-buffer-other-window shell-buffer-name)
    (goto-char (point-max))
    (insert input)
    (comint-send-input)))
;(shell-send-input "ls")


(defun defun-at-point ()
  "Return the text of the defun at point."
  (apply #'buffer-substring-no-properties
         (region-for-defun-at-point)))

(defun region-for-defun-at-point ()
  "Return the start and end position of defun at point."
  (save-excursion
    (save-match-data
      (end-of-defun)
      (let ((end (point)))
        (beginning-of-defun)
        (list (point) end)))))

(defun expression-preceding-point ()
  "Return the expression preceding point as a string."
  (buffer-substring-no-properties
   (save-excursion (backward-sexp) (point))
   (point)))

(defun shell-eval-last-expression ()
  "Send the expression preceding point to the *shell* buffer."
  (interactive)
  (shell-send-input (expression-preceding-point)))

(defun shell-eval-defun ()
  "Send the current toplevel expression to the *shell* buffer."
  (interactive)
  (shell-send-input (defun-at-point)))

(defun shell-eval-region ()
  "Send the current region to the *shell* buffer."
  (interactive)
  (shell-send-input (buffer-substring-no-properties
                     (region-beginning)
                     (region-end))))


(add-hook 'clojure-mode-hook
          '(lambda ()
             (define-key clojure-mode-map (kbd "C-c e") 'shell-eval-last-expression)
             (define-key clojure-mode-map (kbd "C-c x") 'shell-eval-defun)
             (define-key clojure-mode-map (kbd "C-c r") 'shell-eval-region)))

(global-set-key (kbd "C-c e") 'shell-eval-last-expression)
(global-set-key (kbd "C-c x") 'shell-eval-defun)
(global-set-key (kbd "C-c r") 'shell-eval-region)


;; EXPERIMENTAL
(menu-bar-enable-clipboard)


(global-set-key [(control ?.)] 'complete-symbol)

(global-set-key "\C-x\C-g" 'w3m-search)
(global-set-key "\C-x\C-u" 'w3m-browse-url)

(global-set-key "\M-%" 'query-replace-regexp)


;; from http://www.openweblog.com/users/hexmode/532156.html
(global-set-key [(control ?+)] (lambda () (interactive)
                                      (text-scale-increase 1)))
(global-set-key [(control ?-)] (lambda () (interactive)
                                      (text-scale-decrease 1)))
(global-set-key [(control ?0)] (lambda () (interactive)
                                      (text-scale-increase 0)))


;; from http://trey-jackson.blogspot.com/2009/06/emacs-tip-31-kill-other-buffers-of-this.html
(global-set-key (kbd "C-x K") 'kill-other-buffers-of-this-file-name)
(defun kill-other-buffers-of-this-file-name (&optional buffer)
"Kill all other buffers visiting files of the same base name."
(interactive "Buffer to make unique: ")
(setq buffer (get-buffer buffer))
(cond ((buffer-file-name buffer)
       (let ((name (file-name-nondirectory (buffer-file-name buffer))))
         (loop for ob in (buffer-list)
               do (if (and (not (eq ob buffer))
                           (buffer-file-name ob)
                           (let ((ob-file-name (file-name-nondirectory (buffer-file-name ob))))
                             (or (equal ob-file-name name)
                                 (string-match (concat name "\\.~.*~$") ob-file-name))) )
                      (kill-buffer ob)))))
      (default (message "This buffer has no file name."))))


;; from http://www.emacswiki.org/emacs/UnfillParagraph
(defun unfill-paragraph ()
  (interactive)
  (let ((fill-column (point-max)))
    (fill-paragraph nil)))

(defun unfill-region ()
  (interactive)
  (let ((fill-column (point-max)))
    (fill-region (region-beginning) (region-end) nil)))

(define-key global-map "\M-Q" 'unfill-paragraph)
(define-key global-map "\C-\M-q" 'unfill-region)


; from http://stackoverflow.com/questions/12866308/include-date-and-time-of-original-message-in-quoted-reply-using-emacs-and-gnus
(defun mtd-citation-line ()
  "Inserts name, email, and date"
  (when message-reply-headers
    (insert "On "
        (format-time-string "%a, %b %e, %Y at %r"
                (date-to-time (mail-header-date message-reply-headers)))
        ", "
        (or (gnus-extract-address-component-name (mail-header-from message-reply-headers))
        "Martin Dengler")
        (format " <%s>"
            (or (gnus-extract-address-component-email (mail-header-from message-reply-headers))
            "martin@martindengler.com"))
        " wrote:\n")))

;(setq message-citation-line-function 'mtd-citation-line)


;(load-library "~/.emacs.d/site-lisp/zenburn.el")
;(color-theme-zenburn)
;(setq eval-expression-debug-on-error t)


;; from http://www.emacswiki.org/emacs/RevertBuffer
(defun revert-buffer-keep-undo (&rest -)
  "Revert buffer but keep undo history."
  (interactive)
  (let ((inhibit-read-only t))
    (erase-buffer)
    (insert-file-contents (buffer-file-name))
    (set-visited-file-modtime (visited-file-modtime))
    (set-buffer-modified-p nil)))
;(setq revert-buffer-function 'revert-buffer-keep-undo)
;(setq revert-buffer-function 'revert-buffer--default)



;; X-Uniform-Type-Identifier: com.apple.mail-note
(defun apple-note-to-text-hook ()
  "convert apple note html to text for editing"
  ;(when (eq major-mode 'org-mode)
  ;  (shell-command-to-string (format "your-script-name %s" buffer-file-name))))
)
(defun apple-note-from-text-hook ()
  "convert apple note html to text for editing"
  ;(when (eq major-mode 'org-mode)
  ;  (shell-command-to-string (format "your-script-name %s" buffer-file-name))))
)
; (add-hook 'after-save-hook #'apple-note-to-text)



;eval $(cat $(ls -atr ~/.dbus/session-bus/* | tail -1) | grep -v ^# | sed -e 's/^/export /' ) && EMACS_LOAD_LIBS=1 TERM=xterm-256-color GDK_RGBA=0 emacs -nw
;(dbus-init-bus :session)
(put 'upcase-region 'disabled nil)


; disable the "ding" behavior of isearch-wrap-pause during macro execution, as explained in this debian bug: https://debbugs.gnu.org/cgi/bugreport.cgi?bug=66149#19
(defadvice kmacro-call-macro (around align-regexp-with-spaces activate)
  (let ((isearch-wrap-pause 'no-ding))
    ad-do-it))



(fset 'markdown-macro-code-ify-symbol-at-point
      (kmacro-lambda-form [?\M-b ?\C-  ?\M-f ?\C-w ?` ?\C-y ?`] 0 "%d"))
(put 'dired-find-alternate-file 'disabled nil)
