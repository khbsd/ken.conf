call plug#begin('~/.local/share/nvim/plugged')

Plug 'vim-airline/vim-airline-themes'
Plug 'vim-airline/vim-airline'
Plug 'dense-analysis/ale'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'jiangmiao/auto-pairs'
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-vinegar'
Plug 'tpope/vim-sensible'
Plug 'tpope/vim-surround'
Plug 'dense-analysis/ale'
Plug 'nvim-lua/popup.nvim'
Plug 'nvim-telescope/telescope.nvim'
Plug 'dstein64/nvim-scrollview', {'branch':'main'}
Plug 'ingram1107/moneokai'
Plug 'morhetz/gruvbox'
Plug 'junegunn/vim-easy-align'
Plug 'preservim/nerdtree'
Plug 'neoclide/coc.nvim', {'branch':'release'}
Plug 'norcalli/nvim-colorizer.lua'
Plug 'itchyny/calendar.vim'
Plug 'dracula/vim', {'as': 'dracula'}

call plug#end()

set number
set termguicolors
set tabstop=4
set shiftwidth=4
set smartindent
set autoindent

let g:airline_theme="base16_dracula"
let g:airline_powerline_fonts=1
colo dracula
hi normal guibg=000000
lua require'colorizer'.setup()

let g:copilot_no_tab_map = v:true
inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1):
      \ exists('b:_copilot.suggestions') ? copilot#Accept("\<CR>") :
      \ CheckBackSpace() ? "\<Tab>" :
      \ coc#refresh()
