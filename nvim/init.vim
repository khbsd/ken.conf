call plug#begin('~/.local/share/nvim/plugged')

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
Plug 'junegunn/vim-easy-align'
Plug 'preservim/nerdtree'
Plug 'neoclide/coc.nvim', {'branch':'release'}
Plug 'norcalli/nvim-colorizer.lua'
Plug 'itchyny/calendar.vim'

call plug#end()

set number
set termguicolors
set tabstop=4
set shiftwidth=4
set smartindent
set autoindent

colo moneokai
hi normal guibg=000000
lua require'colorizer'.setup()
autocmd VimEnter * NERDTree | wincmd p
